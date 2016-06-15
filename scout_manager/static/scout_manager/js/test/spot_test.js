var assert = require('assert');
var Spot = require('../spot').Spot;
var jsdom = require('jsdom');
var jquery = require('jquery');

var jqueryFromHtml = function jqueryFromHtml(html) {
    var doc = jsdom.jsdom(html);
    var win = doc.parentWindow;
    var $ = jquery(win);
    return $;
}

describe("test test", function() {
    describe("test", function() {
        it('should test', function() {
            global.$ = jqueryFromHtml('<form> <p> </p> </form>');
            assert.equal(true, true);
            Spot.submit_spot();
        });
    });
});
