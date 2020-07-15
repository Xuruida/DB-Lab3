<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0px text-align: center">
      <h1>账户详情 {{ account_id }}</h1>
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
      <!-- savings account -->
      <div style="margin: 0 0 30px">
        <h2>账户客户列表</h2>
        <a-table
          :columns="clientColumns"
          :data-source="clientList"
          row-key="client"
        >
          <span slot="detail" slot-scope="record">
            <a-button @click="deleteClient(record)" type="danger"
              >删除客户</a-button
            >
          </span>
        </a-table>
      </div>
      <div style="margin:20px 0">
        <h2>为该账户添加新客户</h2>
        <a-form
          :form="clform"
          :label-col="{ span: 4 }"
          :wrapper-col="{ span: 12 }"
          @submit="handleSVSubmit"
        >
          <a-form-item label="身份证号">
            <a-input
              v-decorator="['client', { rules: [{ required: true }] }]"
            />
          </a-form-item>
          <a-form-item :wrapper-col="{ span: 12, offset: 2 }">
            <a-button
              style="margin: 15px"
              type="primary"
              html-type="submit"
              @click="handleClientSubmit"
            >
              提交
            </a-button>
          </a-form-item>
        </a-form>
      </div>

      <div v-if="this.is_savings === 'true'">
        <a-descriptions bordered title="详细信息">
          <a-descriptions-item
            v-for="item in savingsLabels"
            :key="item.key"
            :label="item.label"
          >
            {{ detailData[item.key] }}
          </a-descriptions-item>
        </a-descriptions>

        <div style="margin: 40px 0">
          <h1>账户信息修改</h1>
          <a-form
            :form="svform"
            :label-col="{ span: 4 }"
            :wrapper-col="{ span: 12 }"
            @submit="handleSVSubmit"
          >
            <a-form-item
              v-for="item in postSavingsLabels"
              :key="item.key"
              :label="item.label"
            >
              <a-input
                v-decorator="[item.key, { rules: [{ required: true }] }]"
              />
            </a-form-item>
            <a-form-item :wrapper-col="{ span: 12, offset: 2 }">
              <div>
                <a-button
                  style="margin: 15px"
                  type="primary"
                  html-type="submit"
                  @click="handleSVSubmit"
                >
                  提交
                </a-button>
                <a-button
                  style="margin: 15px"
                  @click="
                    () => {
                      let obj = {};
                      for (let k in postSavingsLabels) {
                        key = postSavingsLabels[k]['key'];
                        obj[key] = '';
                      }
                      this.svform.setFieldsValue(obj);
                    }
                  "
                >
                  清空
                </a-button>
                <a-button
                  style="margin: 15px"
                  @click="
                    () => {
                      let obj = {};
                      for (let k in postSavingsLabels) {
                        key = postSavingsLabels[k]['key'];
                        obj[key] = detailData[key];
                      }
                      this.svform.setFieldsValue(obj);
                    }
                  "
                >
                  恢复默认
                </a-button>
              </div>
            </a-form-item>
          </a-form>
        </div>
      </div>

      <!-- checking account -->
      <div v-else>
        <a-descriptions bordered title="详细信息">
          <a-descriptions-item
            v-for="item in checkingLabels"
            :key="item.key"
            :label="item.label"
          >
            {{ detailData[item.key] }}
          </a-descriptions-item>
        </a-descriptions>

        <div style="margin: 40px 0">
          <h1>账户信息修改</h1>
          <a-form
            :form="ckform"
            :label-col="{ span: 4 }"
            :wrapper-col="{ span: 12 }"
            @submit="handleCKSubmit"
          >
            <a-form-item
              v-for="item in postCheckingLabels"
              :key="item.key"
              :label="item.label"
            >
              <a-input
                v-decorator="[item.key, { rules: [{ required: true }] }]"
              />
            </a-form-item>
            <a-form-item :wrapper-col="{ span: 12, offset: 2 }">
              <div>
                <a-button
                  style="margin: 15px"
                  type="primary"
                  html-type="submit"
                  @click="handleCKSubmit"
                >
                  提交
                </a-button>
                <a-button
                  style="margin: 15px"
                  @click="
                    () => {
                      let obj = {};
                      for (let k in postCheckingLabels) {
                        key = postCheckingLabels[k]['key'];
                        obj[key] = '';
                      }
                      this.svform.setFieldsValue(obj);
                    }
                  "
                >
                  清空
                </a-button>
                <a-button
                  style="margin: 15px"
                  @click="
                    () => {
                      let obj = {};
                      for (let k in postCheckingLabels) {
                        key = postCheckingLabels[k]['key'];
                        obj[key] = detailData[key];
                      }
                      this.svform.setFieldsValue(obj);
                    }
                  "
                >
                  恢复默认
                </a-button>
              </div>
            </a-form-item>
          </a-form>
        </div>
      </div>
    </a-layout-content>
  </div>
</template>

<script>
import {
  getAccountDetail,
  getSavingsDetail,
  patchSavings,
  getCheckingDetail,
  patchChecking,
  deleteCA,
  postCA
} from "@/api/api.js";

const clientColumns = [
  {
    title: "身份证号",
    key: "client",
    dataIndex: "client"
  },
  {
    title: "最近访问时间",
    key: "latest_time",
    dataIndex: "latest_time"
  },
  {
    title: "操作",
    key: "detail",
    scopedSlots: { customRender: "detail" }
  }
];

const savingsLabels = [
  {
    label: "账户号",
    key: "account_ID"
  },
  {
    label: "开户日期",
    key: "open_date"
  },
  {
    label: "支行编号",
    key: "branch"
  },
  {
    label: "余额",
    key: "balance"
  },
  {
    label: "利率",
    key: "interest_rate"
  },
  {
    label: "货币种类",
    key: "currency_type"
  }
];

const postSavingsLabels = [
  {
    label: "余额",
    key: "balance"
  },
  {
    label: "利率",
    key: "interest_rate"
  },
  {
    label: "货币种类",
    key: "currency_type"
  }
];

const checkingLabels = [
  {
    label: "账户号",
    key: "account_ID"
  },
  {
    label: "开户日期",
    key: "open_date"
  },
  {
    label: "支行编号",
    key: "branch"
  },
  {
    label: "透支额",
    key: "overdraft"
  }
];

const postCheckingLabels = [
  {
    label: "透支额",
    key: "overdraft"
  }
];

export default {
  data() {
    return {
      savingsLabels,
      postSavingsLabels,
      checkingLabels,
      postCheckingLabels,
      clientColumns,
      detailData: {
        account_ID: "default",
        open_date: "default",
        branch: "default",
        balance: "default",
        interest_rate: "default",
        currency_type: "default",
        overdraft: "default"
      },
      account_id: this.$route.query.account_id,
      is_savings: String(this.$route.query.is_savings),
      id: this.$route.query.id,
      clientList: []
    };
  },

  methods: {
    // Client Management

    getClientList(account_id) {
      getAccountDetail(account_id).then(response => {
        let resData = response.data;
        if (resData.status_code === 0) {
          console.log(resData.data);
          this.clientList = resData.data;
        }
      });
    },

    deleteClient(rec) {
      console.log(rec);
      deleteCA(rec.id)
        .then(response => {
          console.log(response);
          this.$message.success("删除成功");
          this.getClientList(this.account_id);
        })
        .catch(error => {
          this.$message.error(`删除失败. Error: ${error.response.status}`);
        });
    },

    handleClientSubmit(e) {
      e.preventDefault();
      this.clform.validateFields((err, values) => {
        if (!err) {
          values["account"] = this.account_id;
          console.log(values);
          postCA(values)
            .then(response => {
              let resData = response.data;
              if (resData.status_code === 0) {
                console.log(resData.data);
                this.getClientList(this.account_id);
                this.$message.success("添加成功");
              } else {
                this.$message.error("添加失败");
              }
            })
            .catch(error => {
              console.log(error.response);
              this.$message.error(`添加失败 Error: ${error.response.status}`);
            });
        }
      });
    },

    // Savings Account

    getSVDetail(id) {
      getSavingsDetail(id)
        .then(response => {
          console.log(response.data);
          let resData = response.data;
          if (resData.status_code === 0) {
            this.$message.success("查询成功");
            this.detailData = {
              ...resData.data,
              ...resData.data["account_base"]
            };
            console.log(this.detailData);
          } else {
            this.$message.error("查询失败");
          }
        })
        .catch(error => {
          console.log(error);
          this.$message.error(`查询失败. Error: ${error.response.status}`);
        });
    },

    handleSVSubmit(e) {
      e.preventDefault();
      this.svform.validateFields((err, values) => {
        if (!err) {
          console.log(values);
          // patch
          patchSavings(this.id, values)
            .then(response => {
              let resData = response.data;
              if (resData.status_code === 0) {
                console.log(resData.data);
                this.getSVDetail(this.id);
                this.$message.success("修改成功");
              } else {
                this.$message.error("修改失败");
              }
            })
            .catch(error => {
              console.log(error.response);
              this.$message.error("修改失败");
            });
        }
      });
    },

    // Checking Account

    getCKDetail(id) {
      getCheckingDetail(id)
        .then(response => {
          console.log(response.data);
          let resData = response.data;
          if (resData.status_code === 0) {
            this.$message.success("查询成功");
            this.detailData = {
              ...resData.data,
              ...resData.data["account_base"]
            };
            console.log(this.detailData);
          } else {
            this.$message.error("查询失败");
          }
        })
        .catch(error => {
          console.log(error);
          this.$message.error(`查询失败. Error: ${error.response.status}`);
        });
    },

    handleCKSubmit(e) {
      e.preventDefault();
      this.ckform.validateFields((err, values) => {
        if (!err) {
          console.log(values);
          // patch
          patchChecking(this.id, values)
            .then(response => {
              let resData = response.data;
              if (resData.status_code === 0) {
                console.log(resData.data);
                this.getCKDetail(this.id);
                this.$message.success("修改成功");
              } else {
                this.$message.error("修改失败");
              }
            })
            .catch(error => {
              console.log(error.response);
              this.$message.error("修改失败");
            });
        }
      });
    },
  },

  watch: {
    $route(to, from) {
      console.log(to, from);
      if (to.path !== from.path) this.$router.push(to);
    }
  },

  beforeMount() {
    this.account_id = this.$route.query.account_id;
    this.is_savings = String(this.$route.query.is_savings);
    console.log(this.is_savings);
    this.id = this.$route.query.id;
    if (this.is_savings === "true") {
      this.getSVDetail(this.id);
    } else {
      this.getCKDetail(this.id);
    }
    this.getClientList(this.account_id);
  },

  beforeCreate() {
    this.svform = this.$form.createForm(this, { name: "SVAccount" });
    this.ckform = this.$form.createForm(this, { name: "CKAccount" });
    this.clform = this.$form.createForm(this, { name: "Client" });
  }
};
</script>

<style scoped>
* >>> h1 {
  font-size: 2em;
}
</style>
