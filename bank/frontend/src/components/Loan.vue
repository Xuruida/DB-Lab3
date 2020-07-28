<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0px text-align: center">
      <h1>贷款管理</h1>
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
        <h1>贷款列表</h1>
        <a-table :columns="columns" :data-source="loanList" row-key="loan_ID">
          <span slot="detail" slot-scope="record">
            <a-button @click="getDetail(record)">详情</a-button>
          </span>
        </a-table>
        <a-button @click="getLoan()" type="primary" style="margin: 20px"
          >重新获取列表</a-button
        >
      </div>

      <div>
        <h1>添加贷款</h1>
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
import { listLoan, createLoan } from "@/api/api.js";

const columns = [
  {
    title: "贷款号",
    key: "loan_ID",
    dataIndex: "loan_ID"
  },
  {
    title: "支行编号",
    key: "branch",
    dataIndex: "branch"
  },
  {
    title: "总贷款金额",
    key: "total_amount",
    dataIndex: "total_amount"
  },
  {
    title: "客户身份证号",
    key: "clients",
    dataIndex: "clients"
  },
  {
    title: "详情信息",
    key: "detail",
    scopedSlots: { customRender: "detail" }
  }
];

const postItems = [
  {
    label: "贷款号",
    name: "loan_ID"
  },
  {
    label: "支行编号",
    name: "branch"
  },
  {
    label: "总金额",
    name: "total_amount"
  },
  {
    label: "身份证号",
    name: "client_ID"
  }
];

export default {
  data() {
    return {
      loanList: [],
      columns,
      postItems
    };
  },

  beforeMount() {
    this.getLoan();
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Loan" });
  },

  methods: {
    getLoan() {
      listLoan()
        .then(response => {
          let resData = response.data;
          console.log(resData);
          let listData = resData.data;
          this.loanList = listData;
        })
        .catch(error => {
          console.log(error.response);
          this.$message.error(`获取列表失败: Error ${error.response.status}`);
        });
    },

    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log(values);
          values["clients"] = [values["client_ID"]];
          console.log(values);
          createLoan(values)
            .then(response => {
              let resData = response.data;
              if (resData["status_code"] === 0) {
                this.$message.success("贷款添加成功");
                console.log(resData.data);
              } else {
                this.$message.error("贷款添加失败");
              }
              this.getLoan();
            })
            .catch(error => {
              console.log(error.response);
              if (error.response.status === 404) {
                this.$router.push("/404");
              } else {
                this.$message.error(
                  `贷款添加失败: Error ${error.response.status}`
                );
              }
            });
        }
      });
    },

    getDetail(obj) {
      console.log(obj);
      this.$router.push({
        path: `/loan/${obj.loan_ID}`
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
