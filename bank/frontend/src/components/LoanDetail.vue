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
      <div style="margin: 15px 0px">
        <a-descriptions bordered title="基本信息">
          <a-descriptions-item
            v-for="item in labels"
            :key="item.key"
            :label="item.label"
          >
            {{ detailData[item.key] }}
          </a-descriptions-item>
        </a-descriptions>
      </div>

      <div>
        <h2>发放详情</h2>
        <p>当前已发放总额：{{ released_amount }}</p>
        <p>当前待发放余额：{{ remaining_amount }}</p>
        <a-table
          :columns="columns"
          :data-source="releaseList"
          row-key="loan_ID"
        >
        </a-table>
        <a-button @click="getReleaseList()" type="primary" style="margin: 20px"
          >重新获取列表</a-button
        >
      </div>
      <div>
        <h2>发放贷款</h2>
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
import { getLoanDetail, getLoanReleases, createRelease } from "@/api/api.js";

const labels = [
  {
    label: "贷款号",
    key: "loan_ID"
  },
  {
    label: "贷款总额",
    key: "total_amount"
  },
  {
    label: "支行编号",
    key: "branch"
  },
  {
    label: "客户身份证号",
    key: "clients"
  }
];

const columns = [
  {
    title: "发放编号",
    key: "id",
    dataIndex: "id"
  },
  {
    title: "发放金额",
    key: "amount",
    dataIndex: "amount"
  },
  {
    title: "发放时间",
    key: "time",
    dataIndex: "time"
  }
];

const postItems = [
  {
    label: "发放量",
    name: "amount"
  }
];
export default {
  data() {
    return {
      releaseList: [],
      detailData: {
        loan_id: "default",
        total_amount: "default",
        branch: "default",
        clients: "default"
      },
      columns,
      labels,
      postItems,
      loan_id: this.$route.params.loan_id
    };
  },

  computed: {
    released_amount() {
      let tot = 0;
      for (let x in this.releaseList) {
        tot += parseFloat(this.releaseList[x]["amount"]);
      }
      return tot.toFixed(3);
    },

    remaining_amount() {
      let remain =
        parseFloat(this.detailData["total_amount"]) - this.released_amount;
      return remain.toFixed(3);
    }
  },

  beforeMount() {
    this.getDetail();
    this.getReleaseList();
  },

  beforeCreate() {
    this.loan_id = this.$route.params.loan_id;
    this.form = this.$form.createForm(this, { name: "Release" });
  },

  methods: {
    getDetail() {
      getLoanDetail(this.loan_id)
        .then(response => {
          let resData = response.data;
          console.log(resData);
          let detailData = resData.data;
          detailData["clients"] = detailData["clients"][0];
          this.detailData = detailData;
          console.log(this.detailData);
        })
        .catch(error => {
          console.log(error.response);
          this.$message.error(`获取信息失败: Error ${error.response.status}`);
        });
    },

    getReleaseList() {
      getLoanReleases(this.loan_id)
        .then(response => {
          let resData = response.data;
          console.log(resData);
          this.releaseList = resData.data;
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
          values["loan"] = this.loan_id;
          createRelease(values)
            .then(response => {
              let resData = response.data;
              if (resData["status_code"] === 0) {
                this.$message.success("贷款发放成功");
                console.log(resData.data);
              } else {
                this.$message.error("贷款发放失败");
              }
              this.getReleaseList();
            })
            .catch(error => {
              console.log(error.response);
              if (error.response.status === 404) {
                this.$router.push("/404");
              } else {
                this.$message.error(
                  `贷款发放失败: Error ${error.response.status}`
                );
              }
            });
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
