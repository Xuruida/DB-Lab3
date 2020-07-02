<template>
  <a-layout id="homepage-layout" style="min-height: 100vh">
    <a-layout-header class="header" style="height: 100px; color: white">
      <div style="line-height: 50px; font-size: 25px; padding: 25px 0px">
        {{ pageInfo.courseName }} - {{ pageInfo.semester }} -
        {{ pageInfo.courseSubID }}
      </div>
    </a-layout-header>
    <a-layout>
      <a-layout-sider theme="light" style="width: 200px">
        <a-menu
          mode="inline"
          theme="light"
          :default-selected-keys="['1']"
          v-model="selectedKeys"
        >
          <a-menu-item v-for="item in pageInfo.items" :key="item.itemID">
            {{ item.itemName }}
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout-content style="padding: 24px">
        <div
          v-html="selectedItem.content"
          :style="{
            background: '#fff',
            padding: '24px',
            margin: 0,
            minHeight: '400px'
          }"
        ></div>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>
import { getHomepage } from "@/api/api.js";

export default {
  name: "Homepage",
  data() {
    return {
      selectedKeys: ["1"],
      pageInfo: {
        courseName: "courseName",
        semester: "SP2020",
        courseSubID: "01",
        items: [
          {
            itemID: "1",
            itemName: "item1",
            content: "<div><h1>item1</h1></div>"
          },
          {
            itemID: "2",
            itemName: "item2",
            content: "<div><h1>item2</h1></div>"
          }
        ]
      }
    };
  },

  computed: {
    selectedItem() {
      let item, index;
      for (index in this.pageInfo.items) {
        item = this.pageInfo.items[index];
        // console.log(item);
        if (this.selectedKeys[0] == item.itemID) break;
      }
      return item;
    }
  },

  methods: {
    loadHomepage(obj) {
      console.log(obj);
      getHomepage(obj.course_id, obj.semester_id, obj.course_sub_id).then(
        response => {
          let resData = response.data;
          console.log(resData);
          this.pageInfo.courseName = resData[0].course.course;
          this.pageInfo.semester = resData[0].course.semester;
          this.pageInfo.courseSubID = resData[0].course.course_sub_ID;
          this.pageInfo.items = [];
          let index;
          for (index in resData) {
            let newJson = {
              itemID: String(resData[index].item_ID),
              itemName: resData[index].item_name,
              content: resData[index].content
            };
            this.pageInfo.items.push(newJson);
          }
        }
      );
    }
  },

  created() {
    console.log(this.$route.params);
    this.loadHomepage(this.$route.params);
  },

  watch: {
    $route: function(to) {
      this.loadHomepage(to.params);
    }
  }
};
</script>

<style scoped>
* >>> h1 {
  font-size: 2em;
}
</style>
