<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0px text-align: center">
      <h2>客户信息列表</h2>
    </a-layout-header>
    <a-layout-content
      :style="{
        margin: '24px 16px',
        padding: '24px',
        background: '#fff',
        minHeight: '280px',
        height: ''
      }"
    >
      <a-table
        :columns="columns"
        :data-source="clientData.data"
        row-key="ID_number"
      >
        <span slot="action" slot-scope="record">
            <a-button>修改</a-button>
            <a-button type="danger" @click="deleteInfo(record)">删除</a-button>
        </span>
      </a-table>
      <a-button @click="getClient()" type="primary">重新获取客户信息</a-button>
    </a-layout-content>
  </div>
</template>

<script>
import { listClient } from "@/api/api.js";

export default {
  data() {
    return {
      clientData: {
        status_code: 0,
        data: []
      },
      columns: [
        {
          title: "姓名",
          key: "name",
          dataIndex: "name"
        },
        {
          title: "身份证号",
          key: "id_number",
          dataIndex: "ID_number"
        },
        {
          title: "家庭住址",
          key: "address",
          dataIndex: "address"
        },
        {
          title: "操作",
          key: "action",
          scopedSlots: { customRender: "action"}
        }
      ]
    };
  },

  mounted() {
    this.getClient();
  },

  methods: {
    getClient() {
      listClient().then(response => {
        let resData = response.data;
        console.log(resData);
        this.clientData = response.data;
        console.log(this.clientData);
      });
    },

    deleteInfo(record) {
      console.log(record)
    }
  }
};
</script>


