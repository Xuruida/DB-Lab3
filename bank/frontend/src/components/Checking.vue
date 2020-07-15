<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0px text-align: center">
      <h1>储蓄账户管理</h1>
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
      <div>
        <h1>账户列表</h1>
        <a-table
          :columns="columns"
          :data-source="checkingData"
          row-key="account_ID"
        >
          <span slot="detail" slot-scope="record">
            <a-button @click="getDetail(record)">详情</a-button>
          </span>
        </a-table>
        <a-button @click="getChecking()" type="primary" style="margin: 20px"
          >重新获取列表</a-button
        >
      </div>

      <div>
        <h1>添加新储蓄账户</h1>
        <a-form
          :form="form"
          :label-col="{ span: 2 }"
          :wrapper-col="{ span: 12 }"
          @submit="handleSubmit"
        >
          <a-form-item
            v-for="item in postItems"
            :key="item.name"
            :label="item.label"
          >
            <a-input
              v-decorator="[
                item.name,
                {
                  rules: [{ required: true, message: `请输入${item.label}` }]
                }
              ]"
              :placeholder="`请输入${item.label}`"
            />
          </a-form-item>
          <a-form-item :wrapper-col="{ span: 12, offset: 2 }">
            <a-button type="primary" html-type="submit">
              提交
            </a-button>
          </a-form-item>
        </a-form>
      </div>
    </a-layout-content>
  </div>
</template>

<script>
import { listChecking, createChecking } from "@/api/api.js";

const columns = [
  {
    title: "账户号",
    key: "account_ID",
    dataIndex: "account_ID"
  },
  {
    title: "开户日期",
    key: "open_date",
    dataIndex: "open_date"
  },
  {
    title: "支行编号",
    key: "branch",
    dataIndex: "branch"
  },
  {
    title: "透支额",
    key: "overdraft",
    dataIndex: "overdraft"
  },
  {
    title: "详情信息",
    key: "detail",
    scopedSlots: { customRender: "detail" }
  }
];

const postItems = [
  {
    label: "账户号",
    name: "account_ID"
  },
  {
    label: "支行编号",
    name: "branch"
  },
  {
    label: "透支额",
    name: "overdraft"
  }
];

export default {
  data() {
    return {
      checkingData: [],
      columns,
      postItems
    };
  },

  beforeMount() {
    this.getChecking();
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Client" });
  },

  methods: {
    getChecking() {
      console.log("listing...");
      listChecking()
        .then(response => {
          let resData = response.data;
          console.log(resData);
          let listData = resData.data;
          for (let i = 0; i < listData.length; i++) {
            let tmp = listData[i]["account_base"];
            listData[i] = { ...listData[i], ...tmp };
          }
          console.log(listData);
          this.checkingData = listData;
          this.$message.success("列表获取成功");
        })
        .catch(error => {
          console.log(error);
          this.$message.error("添加失败");
        });
    },

    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          values["is_savings"] = false;
          console.log(values);
          values["account_base"] = {};
          values["account_base"]["account_ID"] = values["account_ID"];
          values["account_base"]["is_savings"] = false;
          values["account_base"]["branch"] = values["branch"];
          createChecking(values)
            .then(response => {
              let resData = response.data;
              if (resData["status_code"] === 0) {
                this.$message.success("账户添加成功");
                console.log(resData.data);
              } else {
                this.$message.error("账户添加失败");
              }
              this.getChecking();
            })
            .catch(error => {
              console.log(error.response);
              if (error.response.status === 404) {
                this.$router.push("/404");
              } else {
                this.$message.error(
                  `账户添加失败: Error ${error.response.status}`
                );
              }
            });
        }
      });
    },

    getDetail(obj) {
      console.log(obj);
      this.$router.push({
        path: "/account/",
        query: {
          account_id: obj.account_ID,
          id: obj.id,
          is_savings: obj.is_savings
        }
      });
    }
  }
};
</script>

<style scoped>
* >>> h1 {
  font-size: 2em;
}
</style>
