import axiosInstance from "./index";

const axios = axiosInstance;

const devHost = "http://127.0.0.1:8000/";

export const listClient = () => {
  return axios.get(devHost + "api/client");
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
