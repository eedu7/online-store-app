"use client";

import { QueryClientProvider } from "@tanstack/react-query";
import { getQueryClient } from "./get-query-client";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

export const TanstackReactQueryProvider = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const queryclient = getQueryClient();
  return (
    <QueryClientProvider client={queryclient}>
      {children}
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
};
