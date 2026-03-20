import dotenv from 'dotenv';
dotenv.config();

export const ENV = {
  baseUrl: process.env.BASE_URL || '',
  username: process.env.LOGIN_USERNAME || '',
  password: process.env.LOGIN_PASSWORD || '',
  apiUrl: process.env.API_URL || '',
};