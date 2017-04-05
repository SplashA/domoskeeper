import { Meteor } from 'meteor/meteor';

Meteor.startup(() => {
  // code to run on server at startup
});

Snaps = new Mongo.Collection('snaps');
Snaps.allow({
		insert: function(date) {
			return true;
		},
		remove: function(date) {
			return true;
		},
		update: function(date) {
			return true;
		}
	});

Snaps.allow({
  insert: function(image) {
    return true;
  },
  remove: function(image) {
    return true;
  },
  update: function(image) {
    return true;
  }
});
	console.log("Emission snap OK !");
