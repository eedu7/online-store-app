export interface UserRoles {
  id: string;
  name: string;
}
export interface User {
  id: string;
  username: string;
  email: string;
  first_name?: string;
  last_name?: string;
  profile_pic?: string;
  phone_number?: string;
  phone_verified: boolean;
  is_active: boolean;
  roles: UserRoles[];
}

interface Token {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
}

export interface AuthResponse {
  user: User;
  token: Token;
}

export interface CurrentUser {
  user: User | null;
  isAdmin: boolean;
  isTenant: boolean;
  isCustomer: boolean;
}
