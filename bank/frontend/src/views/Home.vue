<template>
  <a-layout
    id="components-layout-demo-custom-trigger"
    style="min-height: 100vh"
  >
    <a-layout-sider :trigger="null">
      <div class="logo" />
      <a-menu theme="dark" mode="inline">
        <a-menu-item
          @click="
            () => {
              this.$router.push({ path: '/' });
            }
          "
          key="1"
        >
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
          <span>客户管理</span>
        </a-menu-item>
        <a-sub-menu key="account">
          <span slot="title"><span>账户管理</span></span>
          <a-menu-item-group key="g1">
            <a-menu-item
              @click="
                () => {
                  this.$router.push({ path: '/savings' });
                }
              "
              key="3"
            >
              <span>储蓄账户管理</span>
            </a-menu-item>
            <a-menu-item
              @click="
                () => {
                  this.$router.push({ path: '/checking' });
                }
              "
              key="4"
            >
              <span>支票账户管理</span>
            </a-menu-item>
          </a-menu-item-group>
        </a-sub-menu>
        <a-menu-item
          @click="
            () => {
              this.$router.push({ path: '/loan/' });
            }
          "
          key="5"
        >
          <span>贷款管理</span>
        </a-menu-item>
        <a-menu-item
          @click="
            () => {
              this.$router.push({ path: '/stat/' });
            }
          "
          key="6"
        >
          <span>业务统计</span>
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

  watch: {
    $route(to, from) {
      console.log(to, from);
      if (to !== from) this.$router.push(to);
    }
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
