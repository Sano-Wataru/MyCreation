import java.sql.*;
import java.util.*;

class TestDatabaseDriver {
    private static final String DRIVER_NAME = "org.sqlite.JDBC";
    private static final String JDBC_URL = "jdbc:sqlite:D:\\ProgramFile\\DataBase\\sqlite3\\sqlite-tools-win32-x86-3380500\\user.sqlite3";
    public static void main(String[] args) {
        Connection connection = null;
        Statement statement = null;
        try {
            Class.forName(DRIVER_NAME);

            //データベースのPATHを指定。相対パスでも絶対パスでも行けるようです。
            connection = DriverManager.getConnection(JDBC_URL);
            statement = connection.createStatement();
            String sql = "select * from clothes";
            ResultSet rs = statement.executeQuery(sql);
            
            ResultSetMetaData meta = rs.getMetaData();
            List<Clothes> clothes_list = new ArrayList<Clothes>();
            Clothes clothes = new Clothes();
            int data_cnt=0;
            while(rs.next()) {
                clothes.id = rs.getInt(1);
                clothes.name = rs.getString(2);
                clothes.category = rs.getString(3);
                clothes.cindex = rs.getDouble(4);
                clothes_list.add(clothes);
                clothes_list.get(data_cnt).print();
                data_cnt++;
            }
            
        } catch(ClassNotFoundException e) {
            e.printStackTrace();
        } catch(SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if(statement != null) {
                    statement.close();
                }
            } catch(SQLException e) {
                e.printStackTrace();
            }
            try {
                if(connection != null) {
                    connection.close();
                }
            } catch(SQLException e) {
                e.printStackTrace();
            }
        }
    }
}