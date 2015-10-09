/* security */
var express = require('express');
var router = express.Router();


router.use('/security',require('./modules/security') );

module.exports = router;
