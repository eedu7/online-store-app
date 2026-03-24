import { create } from "zustand";
import { createJSONStorage, persist } from "zustand/middleware";
type Store = {
  accessToken?: string;
  refreshToken?: string;
  setToken: (accessToken: string, refreshToken: string) => void;
  clearToken: () => void;
};

export const useAuthStore = create<Store>()(
  persist(
    (set) => ({
      accessToken: undefined,
      refreshToken: undefined,
      setToken: (accessToken, refreshToken) =>
        set({
          accessToken,
          refreshToken,
        }),
      clearToken: () =>
        set({
          accessToken: undefined,
          refreshToken: undefined,
        }),
    }),
    {
      name: "auth-storage",
      storage: createJSONStorage(() => localStorage),
      partialize: (state) => ({
        accessToken: state.accessToken,
        refreshToken: state.refreshToken,
      }),
    },
  ),
);
