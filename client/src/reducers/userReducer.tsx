// src/reducers/userReducer.tsx

export interface UserState {
    isLoggedIn: boolean;
    email: string | null;
  }
  
  const initialState: UserState = {
    isLoggedIn: false,
    email: null,
  };
  
  type UserAction =
    | { type: 'LOGIN'; payload: string }
    | { type: 'LOGOUT' };
  
  const userReducer = (state = initialState, action: UserAction): UserState => {
    switch (action.type) {
      case 'LOGIN':
        return { ...state, isLoggedIn: true, email: action.payload };
      case 'LOGOUT':
        return { ...state, isLoggedIn: false, email: null };
      default:
        return state;
    }
  };
  
  export default userReducer;
  