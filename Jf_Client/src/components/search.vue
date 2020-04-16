<template>
  <div id="search">
    <div class="container-full">
      <el-container>
        <div id="center">
          <el-main>
            <div class="block">
              <el-cascader
                v-model="value"
                :options="options"
                @change="handleChange">
              </el-cascader>
            </div>
            <div class="sea_con">
              <el-table v-loading="loading" :data="tableData" style="width: 100%">
                <el-table-column prop="upload_date" label="上传日期" width="180"></el-table-column>
                <el-table-column prop="creator" label="创作者" width="180"></el-table-column>
                <el-table-column prop="title" label="标题"></el-table-column>
              </el-table>
            </div>
          </el-main>
        </div>
      </el-container>
    </div>
  </div>
</template>

<script>
  export default {
    name: "search",
    data() {
      return {
        tableData: [],
        loading: false,
        value: [],
        options: [
          {
            value: 'jfmt',
            label: '江峰漫谈',
            children: [
              {
                value: '2020-03',
                label: '2020年3月',
              },
              {
                value: '2020-02',
                label: '2020年2月',
              },
              {
                value: '2020-01',
                label: '2020年1月',
              },
              {
                value: '2020-12',
                label: '2019年12月',
              },
              {
                value: '2019-11',
                label: '2019年11月',
              },
              {
                value: '2019-09',
                label: '2019年9月',
              },
              {
                value: '2019-08',
                label: '2019年8月',
              }
            ]
          },
          {
            value: 'today_history',
            label: '历史的今天',
            children: [
              {
                value: '2020-02',
                label: '2020年2月',
              },
              {
                value: '2020-12',
                label: '2019年12月',
              },
              {
                value: '2019-11',
                label: '2019年11月',
              },
              {
                value: '2019-09',
                label: '2019年9月',
              },
              {
                value: '2019-08',
                label: '2019年8月',
              },
              {
                value: '2019-07',
                label: '2019年7月',
              },
              {
                value: '2019-06',
                label: '2019年6月',
              },
            ]
          },
          {
            value: 'trump_twitter',
            label: '川普推推推',
            children: [
              {
                value: '2019-12',
                label: '2019年12月',
              },
              {
                value: '2019-11',
                label: '2019年11月',
              },
              {
                value: '2019-10',
                label: '2019年10月',
              },
              {
                value: '2019-09',
                label: '2019年9月',
              },
              {
                value: '2019-08',
                label: '2019年8月',
              },
              {
                value: '2019-07',
                label: '2019年7月',
              },
              {
                value: '2019-06',
                label: '2019年6月',
              },
            ]
          },
          {
            value: 'wenzhao',
            label: '文昭谈古论今',
            children: [
              {
                value: '2020-04',
                label: '2020年4月',
              },
              {
                value: '2020-03',
                label: '2020年3月',
              },
              {
                value: '2020-01',
                label: '2020年1月',
              },
              {
                value: '2019-12',
                label: '2019年12月',
              },
              {
                value: '2019-11',
                label: '2019年11月',
              },
              {
                value: '2019-10',
                label: '2019年10月',
              },
              {
                value: '2019-09',
                label: '2019年9月',
              }
            ]
          }
        ],
      };
    },
    methods: {
      handleChange(){
        this.$axios.get('/ajax/searchData',
          {
            params: {
              column:this.value[0],
              month: this.value[1]
            }
          }
        ).then(res=>{
          this.tableData = res.data
        })
      }

    },
    mounted() {
    }
  }
</script>

<style>
    * {
        padding: 0;
        margin: 0;
        font-family: Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    }
    #search{
        width: 100%;
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        padding: 0;
        margin: 0;
        background: #f7f7f7;
    }
    #center{
        width: 100%;
        background: #f5f5f5!important;
        display: flex;
        justify-content: center;
        align-items: center;
        height: auto;
    }
    .el-main{
        width: 100% !important;
        max-width: 1260px !important;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }
    .el-select .el-input{
        width: 130px;
    }
    .el-input-group{
        width: 30%;
    }
    .input-with-select .el-input-group__prepend {
        background-color: #fff;
    }
    .sea_con{
        width: 100%;
        height: auto;
        margin: 1rem 0;
        display: flex;
        justify-items: center;
        align-items: center;
    }
</style>