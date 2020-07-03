<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0px text-align: center">
      <h1>客户信息详情</h1>
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
        <a-descriptions bordered title="详细信息">
          <a-descriptions-item
            v-for="item in labels"
            :key="item.key"
            :label="item.label"
          >
            {{ detailData.data[item.key] }}
          </a-descriptions-item>
        </a-descriptions>
      </div>

      <div style="text-align: center; margin: 20px">
        <a-button type="danger" @click="handleDelete">删除客户</a-button>
      </div>
      <div style="margin: 30px 0 0 0">
        <h1>信息修改</h1>
        <a-form
          :form="form"
          :label-col="{ span: 4 }"
          :wrapper-col="{ span: 12 }"
          @submit="handleSubmit"
        >
          <a-form-item
            v-for="item in labels"
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
                @click="handleSubmit"
              >
                提交
              </a-button>
              <a-button
                style="margin: 15px"
                @click="
                  () => {
                    let obj = {};
                    for (let k in detailData.data) obj[k] = '';
                    this.form.setFieldsValue(obj);
                  }
                "
              >
                清空
              </a-button>
              <a-button
                style="margin: 15px"
                @click="
                  () => {
                    this.form.setFieldsValue(detailData.data);
                  }
                "
              >
                恢复默认
              </a-button>
            </div>
          </a-form-item>
        </a-form>
      </div>
    </a-layout-content>
  </div>
</template>

<script>
import {
  getClientDetail,
  putClient,
  patchClient,
  deleteClient
} from "@/api/api.js";

const labels = [
  {
    key: "name",
    label: "姓名"
  },
  {
    key: "ID_number",
    label: "身份证号(不能修改)"
  },
  {
    key: "tel",
    label: "电话号码"
  },
  {
    key: "address",
    label: "家庭住址"
  },
  {
    key: "contact_name",
    label: "联系人姓名"
  },
  {
    key: "contact_tel",
    label: "联系人电话"
  },
  {
    key: "contact_email",
    label: "联系人邮箱"
  },
  {
    key: "relation",
    label: "关系"
  }
];

export default {
  data() {
    return {
      detailData: {
        data: {
          name: "default",
          ID_number: "default",
          tel: "default",
          address: "default",
          contact_name: "default",
          contact_tel: "default",
          contact_email: "default",
          relation: "default"
        }
      },
      IDNumber: this.$route.params.id,
      labels
    };
  },

  methods: {
    getDetail(id) {
      getClientDetail(id)
        .then(response => {
          console.log(response.data);
          this.detailData = response.data;
          this.form.setFieldsValue(this.detailData.data);
        })
        .catch(error => {
          if (error.response.status === 404) {
            this.$router.push("/404");
          } else {
            this.$notification["error"]({
              message: "获取详情",
              description: "遇到未知错误"
            });
          }
        });
    },
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          let isPut = true;
          for (let key in values) {
            if (values[key] === "") {
              delete values.key;
              isPut = false;
            }
          }
          console.log(values, isPut);
          // Put method
          if (isPut)
            putClient(this.IDNumber, values)
              .then(response => {
                if (response.data.status_code === 0) {
                  this.$message.success("修改成功");
                  this.getDetail(response.data.data.ID_number);
                } else {
                  this.$message.error("修改失败");
                }
              })
              .catch(error => {
                console.log(error.response);
                this.$message.error("修改失败");
              });
          // Patch Method
          else
            patchClient(this.IDNumber, values)
              .then(response => {
                if (response.data.status_code === 0) {
                  this.$message.success("修改成功");
                  this.getDetail(response.data.data.ID_number);
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
    // Delete Method
    handleDelete(e) {
      e.preventDefault();
      deleteClient(this.IDNumber)
        .then(response => {
          if (response.data.status_code === 0) {
            this.$message.success("删除成功，跳转回客户列表");
            this.$router.push("/client");
          } else {
            this.$message.error("删除失败");
          }
        })
        .catch(error => {
          console.log(error.response);
          this.$message.error("删除失败");
        });
    }
  },

  watch: {
    $route(to, from) {
      console.log(to, from);
      if (to.path !== from.path) this.$router.push(to);
    }
  },

  beforeMount() {
    this.IDNumber = this.$route.params.id;
    this.getDetail(this.IDNumber);
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Client" });
  }
};
</script>

<style scoped>
* >>> h1 {
  font-size: 2em;
}
</style>
