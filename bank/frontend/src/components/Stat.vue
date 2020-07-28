<template>
  <div>
    <a-layout-header style="background: #fff; padding: 0px text-align: center">
      <h1>统计信息</h1>
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
      <div :key="key">
        <div v-for="item in chartData" :key="item.branch_id">
          <h2>{{ item.branch_id }} - {{ item.name }}</h2>
          <ve-histogram
            :data="item.data"
            :settings="chartSettings"
          ></ve-histogram>
        </div>
      </div>
    </a-layout-content>
  </div>
</template>

<script>
import { getStat } from "@/api/api.js";

const columns = ["time", "loan_amount", "savings_amount", "checking_amount", "release_amount"];
export default {
  data() {
    this.chartSettings = {
      labelMap: {
        loan_amount: "贷款总额",
        savings_amount: "储蓄总额",
        checking_amount: "支票总额",
        release_amount: "发放总额"
      }
    };
    return {
      key: 0,
      statData: [],
      chartData: [
        {
          columns: columns,
          rows: [
            {
              time: "default",
              loan_amount: "default",
              savings_amount: "default",
              checking_amount: "default"
            }
          ]
        }
      ]
    };
  },

  methods: {
    getData() {
      getStat()
        .then(response => {
          let resData = response.data;
          console.log(resData);
          this.statData = resData;
          for (let x in this.statData) {
            this.chartData[x] = {};
            let obj = {
              rows: this.statData[x]["month"],
              columns: columns
            };
            this.chartData[x]["data"] = obj;
            this.chartData[x]["branch_id"] = this.statData[x]["branch_id"];
            this.chartData[x]["city"] = this.statData[x]["city"];
            this.chartData[x]["name"] = this.statData[x]["name"];
          }
          console.log(this.chartData);
          this.key++;
        })
        .catch();
    }
  },

  beforeMount() {
    this.getData();
  }
};
</script>

<style scoped>
* >>> h1 {
  font-size: 2em;
}
</style>
