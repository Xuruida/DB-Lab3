import axiosInstance from "./index";

const axios = axiosInstance;

const devHost = "http://127.0.0.1:8000/";

export const listClient = () => {
  return axios.get(devHost + "api/client/");
};

export const createClient = postData => {
  return axios.post(devHost + "api/client/", postData);
};

export const getClientDetail = id => {
  return axios.get(devHost + `api/client/${id}/`);
};

export const putClient = (id, params) => {
  return axios.put(devHost + `api/client/${id}/`, params);
};

export const patchClient = (id, params) => {
  return axios.patch(devHost + `api/client/${id}/`, params);
};

export const deleteClient = id => {
  return axios.delete(devHost + `api/client/${id}/`);
};

// Savings

export const listSavings = () => {
  return axios.get(devHost + `api/savings`);
};

export const createSavings = postData => {
  return axios.post(devHost + `api/savings/`, postData);
};

export const getSavingsDetail = id => {
  return axios.get(devHost + `api/savings/${id}`);
};

export const patchSavings = (id, params) => {
  return axios.patch(devHost + `api/savings/${id}/`, params);
};

export const deleteSavings = id => {
  return axios.delete(devHost + `api/savings/${id}/`);
};

// Checking

export const listChecking = () => {
  return axios.get(devHost + `api/checking`);
};

export const createChecking = postData => {
  return axios.post(devHost + `api/checking/`, postData);
};

export const getCheckingDetail = id => {
  return axios.get(devHost + `api/checking/${id}`);
};

export const patchChecking = (id, params) => {
  return axios.patch(devHost + `api/checking/${id}/`, params);
};

export const deleteChecking = id => {
  return axios.delete(devHost + `api/checking/${id}/`);
};

// Account Detail

export const getAccountDetail = account_ID => {
  return axios.get(devHost + `api/account/`, {
    params: {
      account_id: account_ID
    }
  });
};

export const deleteCA = id => {
  return axios.delete(devHost + `api/account/${id}`);
};

export const postCA = params => {
  return axios.post(devHost + `api/account/`, params);
};

// Loan

export const listLoan = () => {
  return axios.get(devHost + `api/loan/`);
};

export const createLoan = params => {
  return axios.post(devHost + `api/loan/`, params);
};

export const deleteLoan = loan_id => {
  return axios.delete(devHost + `api/loan/${loan_id}`);
};

// Loan Release

export const listRelease = () => {
  return axios.get(devHost + `api/release/`);
};

export const getLoanReleases = loan_id => {
  return axios.get(devHost + `api/release/`, {
    params: {
      loan_id: loan_id
    }
  });
};

/*
export const getHomepage = (course_id, semester_id, course_sub_id) => {
  console.log(devHost + "api/homepage/get_homepage");
  return axios.get(devHost + "api/homepage/get_homepage", {
    params: {
      course_id: course_id,
      semester_id: semester_id,
      course_sub_id: course_sub_id
    }
  });
};
*/
