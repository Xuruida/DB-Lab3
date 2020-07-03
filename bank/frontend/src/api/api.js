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
