<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0px text-align: center">
      <h1>客户管理</h1>
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
        <h1>客户列表</h1>
        <a-table
          :columns="columns"
          :data-source="clientData.data"
          row-key="ID_number"
        >
          <span slot="detail" slot-scope="record">
            <a-button @click="getDetail(record.ID_number)">详情</a-button>
          </span>
        </a-table>
        <a-button @click="getClient()" type="primary" style="margin: 20px"
          >重新获取客户信息</a-button
        >
      </div>

      <div>
        <h1>添加新客户</h1>
        <a-form
          :form="form"
          :label-col="{ span: 2 }"
          :wrapper-col="{ span: 12 }"
          @submit="handleSubmit"
        >
          <a-form-item label="姓名">
            <a-input
              v-decorator="[
                'name',
                {
                  rules: [{ required: true, message: '请输入姓名' }]
                }
              ]"
              placeholder="请输入姓名"
            />
          </a-form-item>
          <a-form-item label="身份证号">
            <a-input
              v-decorator="[
                'ID_number',
                {
                  rules: [{ required: true, message: '请输入身份证号' }]
                }
              ]"
              placeholder="请输入身份证号"
            />
          </a-form-item>
          <a-form-item label="电话号码">
            <a-input
              v-decorator="[
                'tel',
                {
                  rules: [{ required: true, message: '请输入电话号码' }]
                }
              ]"
              placeholder="请输入电话号码"
            />
          </a-form-item>
          <a-form-item label="家庭住址">
            <a-input
              v-decorator="[
                'address',
                {
                  rules: [{ required: true, message: '请输入家庭住址' }]
                }
              ]"
              placeholder="请输入家庭住址"
            />
          </a-form-item>
          <a-form-item label="联系人姓名">
            <a-input
              v-decorator="[
                'contact_name',
                {
                  rules: [{ required: true, message: '请输入联系人姓名' }]
                }
              ]"
              placeholder="请输入联系人姓名"
            />
          </a-form-item>
          <a-form-item label="联系人电话">
            <a-input
              v-decorator="[
                'contact_tel',
                {
                  rules: [{ required: true, message: '请输入联系人电话' }]
                }
              ]"
              placeholder="请输入联系人电话"
            />
          </a-form-item>
          <a-form-item label="联系人邮箱">
            <a-input
              v-decorator="[
                'contact_email',
                {
                  rules: [{ required: true, message: '请输入联系人邮箱' }]
                }
              ]"
              placeholder="请输入联系人邮箱"
            />
          </a-form-item>
          <a-form-item label="关系">
            <a-input
              v-decorator="[
                'relation',
                {
                  rules: [{ required: true, message: '请输入关系' }]
                }
              ]"
              placeholder="请输入关系"
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
import { listClient, createClient } from "@/api/api.js";

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
          title: "详情信息",
          key: "detail",
          scopedSlots: { customRender: "detail" }
        }
      ]
    };
  },

  beforeMount() {
    this.getClient();
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Client" });
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
        this.clientData = response.data;
        this.$message.success("列表获取成功");
      });
    },

    getDetail(idNum) {
      this.$router.push(`client/${idNum}`);
    },

    deleteInfo(record) {
      console.log(record);
    },

    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
          createClient(values)
            .then(response => {
              let resData = response.data;
              console.log(resData);
              if ("status_code" in resData && resData.status_code === 0) {
                this.$message.success("添加成功");
              } else {
                this.$message.error("添加失败");
              }
              this.getClient();
            })
            .catch(error => {
              console.log(error.response);
              let errMsg = "";
              for (let key in error.response.data) {
                errMsg += `${key}: ${error.response.data[key]}\n`;
              }
              this.$notification["error"]({
                message: "添加失败",
                description: errMsg
              });
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
