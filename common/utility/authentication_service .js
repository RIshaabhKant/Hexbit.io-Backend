const jwt = require('jsonwebtoken');
const { UserProfile } = require('./models'); // Assuming you have a UserProfile model

function getTokensForUser(user) {
  const refreshToken = generateRefreshToken(user);
  const accessToken = generateAccessToken(user);
  return {
    refresh: refreshToken,
    access: accessToken
  };
}

function generateRefreshToken(user) {
  const refreshToken = jwt.sign({ userId: user.id }, 'your-refresh-secret-key', { expiresIn: '7d' });
  return refreshToken;
}

function generateAccessToken(user) {
  const accessToken = jwt.sign({ userId: user.id }, 'your-access-secret-key', { expiresIn: '15m' });
  return accessToken;
}

function getUserForRequest(request) {
  const authorizationHeader = request.headers.authorization;
  if (authorizationHeader && authorizationHeader.startsWith('Bearer ')) {
    const token = authorizationHeader.slice(7); // Remove 'Bearer ' prefix
    try {
      const decodedToken = jwt.verify(token, 'your-access-secret-key');
      const userId = decodedToken.userId;
      // Retrieve the user from the database based on the userId
      const user = UserProfile.findOne({ id: userId });
      return user;
    } catch (error) {
      // Token verification failed
      return null;
    }
  } else {
    // No authorization header or invalid format
    return null;
  }
}

module.exports = {
  getTokensForUser,
  getUserForRequest
};
// Please note that you need to replace 'your-refresh-secret-key' and 'your-access-secret-key' 
// with your own secret keys 

// adapt it based on your specific requirements and the 
// packages you're using in your Node.js projec