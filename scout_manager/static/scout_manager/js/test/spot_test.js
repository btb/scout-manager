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

describe("Spot Tests", function() {
    describe("Submit Spot", function() {
        describe("Create Spot", function() {       
            it('should alert that there was a success', function() {
                global.$ = jqueryFromHtml('<form> <div class="alert hidden" id="pub_error"> </div> </form>');
                Spot.submit_spot();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-success');
            });
            it('should alert that there was a failure', function() {
                global.$ = jqueryFromHtml('<form> <div class="alert hidden" id="pub_error"> </div> </form>');
                Spot.submit_spot();
                assert.equal();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-danger');
            });
        });
        describe("Edit Spot", function() {       
            it('should alert that there was a success', function() {
                global.$ = jqueryFromHtml('<form> <div class="alert hidden" id="pub_error"> </div> </form>');
                Spot.submit_spot();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-success');
            });
            it('should alert that there was a failure', function() {
                global.$ = jqueryFromHtml('<form> <div class="alert hidden" id="pub_error"> </div> </form>');
                Spot.submit_spot();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-danger');
            });
        });

    });
});
