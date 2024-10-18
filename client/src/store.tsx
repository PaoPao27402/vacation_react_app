// src/store.tsx

import { configureStore } from '@reduxjs/toolkit';
import rootReducer from './reducers'; 

// Create the store
const store = configureStore({
  reducer: rootReducer,
  // Redux Toolkit includes redux-thunk by default, so you can omit this unless you need to customize
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware(), // No need to explicitly add thunk unless you want custom middleware
});

export default store;

// Optional: Define RootState and AppDispatch types for TypeScript
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
