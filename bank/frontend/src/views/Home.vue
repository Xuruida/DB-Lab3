<template>
  <a-layout
    id="components-layout-demo-custom-trigger"
    style="min-height: 100vh"
  >
    <a-layout-sider :trigger="null">
      <div class="logo" />
      <a-menu theme="dark" mode="inline" :default-selected-keys="['1']">
        <a-menu-item
          @click="
            () => {
              this.$router.push({ path: '/' });
            }
          "
          key="1"
        >
          <a-icon type="user" />
          <span>主页</span>
        </a-menu-item>
        <a-menu-item
          @click="
            () => {
              this.$router.push({ path: '/client' });
            }
          "
          key="2"
        >
          <a-icon type="video-camera" />
          <span>客户管理</span>
        </a-menu-item>
        <a-menu-item key="3">
          <a-icon type="upload" />
          <span>账户管理</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <router-view></router-view>
    </a-layout>
  </a-layout>
</template>
<script>
import { listClient } from "@/api/api.js";

export default {
  data() {
    return {
      returned_data: "Default"
    };
  },

  methods: {
    getClient() {
      listClient().then(response => {
        let resData = response.data;
        console.log(resData);
      });
    },

    jumpTo() {
      this.$router.push({
        path: "/bank"
      });
    }
  }
};
</script>
<style>
#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

#components-layout-demo-custom-trigger .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}

* >>> h1 {
  font-size: 2em;
}
</style>
