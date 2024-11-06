// src/reducers/userReducer.tsx

import { AnyAction } from 'redux';

export interface User {
  password: string;
  is_superuser: number;
  first_name: string;
  last_name: string;
  email: string;
}

type UserState = User | null;

// Define action types
interface UserLoggedInAction {
  type: 'USER_LOGGED_IN';
  payload: User;
}

interface LogoutAction {
  type: 'LOGOUT';
}

type UserActionTypes = UserLoggedInAction | LogoutAction;

const userReducer = (
  state: UserState = null, 
  action: UserActionTypes | AnyAction
): UserState => {
  switch (action.type) {
    case 'USER_LOGGED_IN':
      return action.payload;

    case 'LOGOUT':
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      return null;

    default:
      return state;
  }
};

export default userReducer;