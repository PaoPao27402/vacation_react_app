// src/store.tsx

import { configureStore, Middleware } from '@reduxjs/toolkit';
import rootReducer, { RootState } from './reducers';

// Load initial state from localStorage
const loadState = (): Partial<RootState> | undefined => {
  try {
    const user = localStorage.getItem('user');
    const token = localStorage.getItem('token');
    
    if (user && token) {
      return {
        user: JSON.parse(user)
      };
    }
  } catch (err) {
    console.log('Error loading state:', err);
  }
  return undefined;
};

// Middleware to persist state to localStorage
const persistMiddleware: Middleware = (store) => (next) => (action: any) => {
  const result = next(action);
  if (action.type === 'USER_LOGGED_IN' || action.type === 'LOGOUT') {
    const state = store.getState();
    if (state.user) {
      localStorage.setItem('user', JSON.stringify(state.user));
    } else {
      localStorage.removeItem('user');
      localStorage.removeItem('token');
    }
  }
  return result;
};

const store = configureStore({
  reducer: rootReducer,
  preloadedState: loadState(),
  middleware: (getDefaultMiddleware) => 
    getDefaultMiddleware().concat(persistMiddleware)
});

export type AppDispatch = typeof store.dispatch;
export default store;