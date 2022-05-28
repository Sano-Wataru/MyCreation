import java.util.*;
import java.sql.*;

class Database {
    private static final String DRIVER_NAME = "org.sqlite.JDBC";
    private static final String JDBC_URL = "jdbc:sqlite:D:\\ProgramFile\\DataBase\\sqlite3\\sqlite-tools-win32-x86-3380500\\user.sqlite3";

    Connection connection = null;
    Statement statement = null;
    ResultSet result = null;

    Database() {
        try {
            Class.forName(DRIVER_NAME);

            connection = DriverManager.getConnection(JDBC_URL);
            statement = connection.createStatement();
        } catch(ClassNotFoundException e) {
            e.printStackTrace();
        } catch(SQLException e) {
            e.printStackTrace();
        }
    }

    List<List<String>> Get(String order) {
        List<List<String>> list_2D = new ArrayList<List<String>>();
        
        try {
            result = statement.executeQuery(order);
            ResultSetMetaData meta = result.getMetaData();
            while(result.next()) {
                List<String> list = new ArrayList<String>();
                list_2D.add(list);
                for(int i=0; i<meta.getColumnCount(); ++i) {
                    list.add(result.getString(i+1));
                }
            }
        } catch(SQLException e){
            e.printStackTrace();
        }
        return list_2D;
    }

    void Close() {
        try {
            connection.close();
        } catch(SQLException e) {
            if(connection != null) {
                e.printStackTrace();
            }
        }
        try {
            statement.close();
        } catch(SQLException e) {
            if(statement != null) {
                e.printStackTrace();
            }
        }
    }
}