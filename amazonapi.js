/* v1: Find price by product IDs from Amazon URL <-- Complete with sample testID
   v2: Find price by generic item name (cup, brush, toothbrush)

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

/*opHelper.execute('ItemLookup', {
  //'SearchIndex': 'Books',
  //'Keywords': 'Andis 17150 Profoil Lithium',
  'ItemId': 'B000LNB8HK',
  'ResponseGroup': 'ItemAttributes'
}).then((response) => {
    //console.log("Results object: ", response.result);

    //console.log("Raw response body: ", response.responseBody) <--- Use to view total structure 

	var xml = response.responseBody;

	const dom = new JSDOM(xml);
	
	console.log(dom.window.document.querySelector("FormattedPrice").textContent);
	}

).catch((err) => {
    console.error("Something went wrong! ", err);
	});
*/
opHelper.execute('ItemSearch', {
  //'SearchIndex': 'Books',
   'Keywords': 'cup',
   'ItemPage': 3,
  'ResponseGroup': 'ItemAttributes'
}).then((response) => {
    //console.log("Results object: ", response.result);

    //console.log("Raw response body: ", response.responseBody) <--- Use to view total structure 

	var xml = response.responseBody;

	const dom = new JSDOM(xml);

	console.log(xml)
	
	//console.log(dom.window.document.querySelector("FormattedPrice").textContent);
	}

).catch((err) => {
    console.error("Something went wrong! ", err);
	});
