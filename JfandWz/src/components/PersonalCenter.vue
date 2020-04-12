<template>
    <div id="PersonalCenter">
        <el-container>
            <div id="center">
                <el-main>
                    <el-table
    :data="tableData"
    style="width: 100%">
                        <el-table-column
                          label="所属栏目"
                          width="180">
                          <template slot-scope="scope">
                            <span style="margin-left: 10px">{{ scope.row.date }}</span>
                          </template>
                        </el-table-column>
                        <el-table-column
                          label="创作者"
                          width="180">
                          <template slot-scope="scope">
                            <el-popover trigger="hover" placement="top">
                              <p>姓名: {{ scope.row.name }}</p>
                              <p>住址: {{ scope.row.address }}</p>
                              <div slot="reference" class="name-wrapper">
                                <el-tag size="medium">{{ scope.row.name }}</el-tag>
                              </div>
                            </el-popover>
                          </template>
                        </el-table-column>
                        <el-table-column label="操作">
                            <template slot-scope="scope">
                                <el-button
                              size="mini"
                              type="danger"
                              @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                            </template>
                        </el-table-column>
                        </el-table>
                </el-main>
            </div>
        </el-container>
    </div>
</template>
<script>
    export default {
        name: "PersonalCenter",
        data() {
            return {
        tableData: [
            {
              date: '江峰漫谈',
              name: '江峰',
              address: '上海市普陀区金沙江路 1518 弄'
            }, {
          date: '文昭谈古论今',
          name: '文昭',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '江峰漫谈',
          name: '江峰',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '历史上的今天',
          name: '江峰',
          address: '上海市普陀区金沙江路 1516 弄'
        }]
      }
        },
        methods: {
            handleDelete(index, row) {
                this.tableData.splice(index,1)
                console.log(index, row);
            }
        }
    }
</script>
<style scoped>
     * {
        padding: 0;
        margin: 0;
        font-family: Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    }
    #PersonalCenter {
        width: 100%;
        height: 100%;
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        padding: 0;
        margin: 0;
        position: fixed;
        background: #f7f7f7;
    }
    .el-container{
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    #center{
        width: 100%;
        background: #f5f5f5!important;
        height: auto;
    }
    .el-main{
        width: 100%!important;
        max-width: 1260px!important;
        margin: 2rem auto;
        padding: 0 1.5rem;
    }
    .el-button{
        padding: .3rem .6rem;
    }
    .el-tag{
        padding: 0 .6rem;
    }
</style>