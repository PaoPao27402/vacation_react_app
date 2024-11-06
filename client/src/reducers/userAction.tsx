// src/reducers/userActions.tsx

import { User } from './userReducer';

export const USER_LOGGED_IN = 'USER_LOGGED_IN';
export const LOGOUT = 'LOGOUT';

export const userLoggedIn = (user: User) => ({
  type: USER_LOGGED_IN,
  payload: user,
});

export const userLogout = () => ({
  type: LOGOUT,
});

export type UserActionTypes = ReturnType<typeof userLoggedIn> | ReturnType<typeof userLogout>;