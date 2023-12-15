import axios, { AxiosError } from 'axios';
import api from '.';

export const userCheckApi = async () => {
  try {
    const endpoint = `/api/accounts/user/`;
    const response = await api.get(endpoint);
    return response;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      // Axios 에러인 경우, HTTP 상태 코드 확인
      const axiosError = error as AxiosError;
      if (axiosError.response && axiosError.response.status === 401) {
        // 상태 코드가 401인 경우, 응답을 반환
        return axiosError.response;
      }
    }
    // 그 외의 경우, 에러를 던짐
    throw error;
  }
};
