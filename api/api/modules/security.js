/* security */
var express = require('express');
var router = express.Router();

/* login. */
router.get('/login', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
