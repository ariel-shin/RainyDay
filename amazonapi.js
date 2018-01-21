/* v1: Find price by product IDs from Amazon URL <-- Complete with sample testID
   v2: Find price by generic item name (cup, brush, toothbrush) <--- Complete with cup test, try to specify searchIndex 

  ################	
  # Dependencies #          
  ################
   npm install jsdom <- xml element printing by ID
   npm install apac  <- nodejs wrapper of Amazon Product Advertising API
*/

const jsdom = require("jsdom");

const { JSDOM } = jsdom;

const {OperationHelper} = require('apac');

const opHelper = new OperationHelper({
    awsId:     'AKIAISF2B2SBCCCDF7LA',
    awsSecret: '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',
    assocId:   'rainyday0d-20' 
});

var itemsValue = 0 

var keyword = null

var departments = {
	Appliances:2619526011,
	ArtsAndCrafts:2617942011,
	Beauty:11055981,
	Books:1000,
	Electronics:493964,
	HealthPersonalCare:3760931,
	Movies:2625374011,
	Music:301668,
	OfficeProducts:1084128,
	SportingGoods:3375301,
	Tools:468240,
	Toys:165795011,
	VideoGames:11846801,
	Wireless:2335753011
};

opHelper.execute('ItemLookup', {
  'ItemId': 'B000LNB8HK', // MUST specify ItemId for results 
  'ResponseGroup': 'ItemAttributes'
}).then((response) => {

    //console.log("Raw response body: ", response.responseBody) <--- Use to view total structure 

	var xml = response.responseBody;

	const dom = new JSDOM(xml);
	
	console.log('Example of Andis 17150 Profoil Lithium: ', dom.window.document.querySelector("FormattedPrice").textContent);
	}

).catch((err) => {
    console.error("Something went wrong! ", err);
	});

opHelper.execute('ItemSearch', {
  'SearchIndex': 'Appliances', // <--- MUST specify SearchIndex for results +  will generalize based on keywords 
   'Keywords': 'toaster',
   'BrowseNode': 2619526011,   // <--- Will generalize to a value based on item department 
  'ResponseGroup': 'OfferSummary'
}).then((response) => {

    //console.log("Raw response body: ", response.responseBody) <--- Use to view total structure 

	var xml = response.responseBody;

	const dom = new JSDOM(xml);
	
	console.log('Example of first cup element: ', dom.window.document.querySelector("FormattedPrice").textContent);
	itemsValue += dom.window.document.querySelector("FormattedPrice").textContent
	console.log("The total value of your items is:", itemsValue.substr(1))
	}

).catch((err) => {
    console.error("Something went wrong! ", err);
	});
