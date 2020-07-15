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
          :data-source="savingsData"
          row-key="account_ID"
        >
          <span slot="detail" slot-scope="record">
            <a-button @click="getDetail(record)">详情</a-button>
          </span>
        </a-table>
        <a-button @click="getSavings()" type="primary" style="margin: 20px"
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
import { listSavings, createSavings } from "@/api/api.js";

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
    title: "余额",
    key: "balance",
    dataIndex: "balance"
  },
  {
    title: "利率",
    key: "interest_rate",
    dataIndex: "interest_rate"
  },
  {
    title: "货币种类",
    key: "currency_type",
    dataIndex: "currency_type"
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
    label: "余额",
    name: "balance"
  },
  {
    label: "利率",
    name: "interest_rate"
  },
  {
    label: "货币种类",
    name: "currency_type"
  }
];

export default {
  data() {
    return {
      savingsData: [],
      columns,
      postItems
    };
  },

  beforeMount() {
    this.getSavings();
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Client" });
  },

  methods: {
    getSavings() {
      console.log("listing...");
      listSavings()
        .then(response => {
          let resData = response.data;
          console.log(resData);
          let listData = resData.data;
          for (let i = 0; i < listData.length; i++) {
            let tmp = listData[i]["account_base"];
            listData[i] = { ...listData[i], ...tmp };
          }
          console.log(listData);
          this.savingsData = listData;
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
          values["is_savings"] = true;
          console.log(values);
          values["account_base"] = {};
          values["account_base"]["account_ID"] = values["account_ID"];
          values["account_base"]["is_savings"] = true;
          values["account_base"]["branch"] = values["branch"];
          createSavings(values)
            .then(response => {
              let resData = response.data;
              if (resData["status_code"] === 0) {
                this.$message.success("账户添加成功");
                console.log(resData.data);
              } else {
                this.$message.error("账户添加失败");
              }
              this.getSavings();
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
