<template>
    <div id="search">
        <div class="container-full">
            <el-container>
                <div id="center">
                    <el-main>
                        <el-input placeholder="请输入内容" v-model="input" class="input-with-select">
    <el-select v-model="select" slot="prepend" placeholder="请选择">
      <el-option label="通过期数查询" value="1"></el-option>
      <el-option label="通过关键字查询" value="2"></el-option>
      <el-option label="通过日期查询" value="3"></el-option>
    </el-select>
    <el-button slot="append" icon="el-icon-search"></el-button>
  </el-input>
                        <div class="sea_con">
                             <el-table
    v-loading="loading"
    :data="tableData"
    style="width: 100%">
    <el-table-column
      prop="date"
      label="上传日期"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="创作者"
      width="180">
    </el-table-column>
    <el-table-column
      prop="address"
      label="标题">
    </el-table-column>
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
          input: '',
        select: '',
          tableData: [{
          date: '2020-04-01',
          name: '文昭谈古论今',
          address: '糧食短缺迫近，要備糧備荒嗎？川普做最壞交底，習近平呢？（文昭談古論今20200401第728期）'
        }, {
          date: '2020-03-18',
          name: '文昭谈古论今',
          address: '中共驱逐美国记者，川普偷着乐；欧美“佛系”vs大国铁腕，谁将胜出（20200318第720期）'
        }, {
          date: '2020-02-06',
          name: '江峰漫谈',
          address: '“是美军带到中国的！” 中共外交部惹恼川普？默克尔称德国将有5000万人受影響，美国NBA停赛，汤姆·汉克斯确诊，国会议员在家辦公，這一切離普通人有多远？（江峰漫談20200312第135期）'
        }],
        loading: true
      };
    },
    methods: {

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