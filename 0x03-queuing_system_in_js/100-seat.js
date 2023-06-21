const express = require('express');
const { createClient } = require('redis');
const { promisify } = require('util');

const app = express();
const client = createClient();
const port = 1245;