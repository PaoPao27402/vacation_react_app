// src/reducers/index.tsx

import { combineReducers } from '@reduxjs/toolkit';
import userReducer from './userReducer';

// Combine reducers correctly
const rootReducer = combineReducers({
  user: userReducer,  
});

// Infer RootState from rootReducer to ensure typing
export type RootState = ReturnType<typeof rootReducer>;

export default rootReducer;