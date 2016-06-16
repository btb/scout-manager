var assert = require('assert');
var Spot = require('../spot').Spot;
var jsdom = require('jsdom');
var jquery = require('jquery');
var Cookies = require('js-cookie');
var ajax = require('ajax');

var jqueryFromHtml = function jqueryFromHtml(html) {
    var doc = jsdom.jsdom(html);
    var win = doc.parentWindow;
    var $ = jquery(win);
    // Function to serialize form data into an JS object
    // (Takes html from the form and sorts it into a 
    // valid dictionary
    $.fn.serializeObject = function() {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function() {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    }; 
    return $;
}

describe("Spot Tests", function() {
    describe("Submit Spot", function() {
        describe("Create Spot", function() { 
            beforeEach(function() {
                global.Cookies = Cookies;
                // By not having an id in the html, the program should recognize to CREATE
                global.$ = jqueryFromHtml('<form> <div class="alert hidden" id="pub_error"> </div>');
            });
            it('should alert that there was a success', function() {
                // to be completed (figure out how to get a valid spot)
                Spot.submit_spot();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-success');
            });
            it('should alert that there was a failure', function() {
                Spot.submit_spot();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-danger');
            });
        });
        describe("Edit Spot", function() {       
            beforeEach(function() {
                global.Cookies = Cookies;
                // By having an hidden id in the html, the program should recognize to EDIT
                global.$ = jqueryFromHtml('<form> <div class="alert hidden" id="pub_error"> </div>' + 
                                          '<input name="id" type="hidden" value="1"> </form>');
            });
            it('should alert that there was a success', function() {
                // to be completed (figure out how to get a valid spot)
                Spot.submit_spot();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-success');
            });
            it('should alert that there was a failure', function() {
                Spot.submit_spot();
                var error = $("#pub_error");
                var classes = error.attr("class");
                assert.equal(classes, 'alert alert-danger');
            });
        });

    });
});
