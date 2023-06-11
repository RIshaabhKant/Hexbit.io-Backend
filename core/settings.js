const path = require('path');
const jwt = require('jsonwebtoken');

const SECRET_KEY = 'django-insecure-1e62wh5t-ruupa8y4oaxyx=9n%xwo&ay(m^ddet0k1fd$lob4w';
const ACCESS_TOKEN_LIFETIME = '5m';
const REFRESH_TOKEN_LIFETIME = '10d';

const BASE_DIR = path.resolve(__dirname, '..');

const DATABASES = {
  default: {
    ENGINE: 'django.db.backends.sqlite3',
    NAME: path.join(BASE_DIR, 'db.sqlite3'),
  },
};

const AUTH_USER_MODEL = 'userprofile.UserProfile';

const config = {
  SECRET_KEY,
  ACCESS_TOKEN_LIFETIME,
  REFRESH_TOKEN_LIFETIME,
  DATABASES,
  AUTH_USER_MODEL,
};

module.exports = config;
