package com.company;

import java.sql.*;
import java.util.ArrayList;

public class AddressBook {
    public Connection conn;

    /**
     * establish connection with mysql server
     *
     * @param database database
     * @param user     user
     * @param password password
     */
    public AddressBook(String database, String user, String password) {
        try {
            // connection to mysql
            String url = "jdbc:mysql://localhost:3307/" + database;
            this.conn = DriverManager.getConnection(url, user, password);
            // TODO: log messages handling
            System.out.println("Everything OK");
        } catch (SQLException e) {
            // TODO: connection error dialog
            e.printStackTrace();
        }
    }

    /**
     * get every contact in database
     *
     * @return list with every contact in database
     */
    public ArrayList<Contact> getContacts() {
        ArrayList<Contact> result = new ArrayList<Contact>();
        PreparedStatement stmt;
        try {
            stmt = this.conn.prepareStatement("Select * From contactos");
            // executeQuery for query (select) sentences
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                result.add(new Contact(rs.getString("nombre"), rs.getString("telefono")));
            }
        } catch (SQLException e) {
            // TODO: error handling
            e.printStackTrace();
        }
        return result;
    }

    /**
     * update contact information in database
     *
     * @param oldName      old name
     * @param newName      new name
     * @param newTelephone new telephone
     * @return
     */
    public int update(String oldName, String newName, String newTelephone) {
        try {
            PreparedStatement stmt = this.conn.prepareStatement("Update contactos Set nombre=?, telefono=? Where nombre=?");
            stmt.setString(1, newName);
            stmt.setString(2, newTelephone);
            stmt.setString(3, oldName);
            // TODO: log messages handling
            System.out.println(stmt.toString());
            // executeQuery for DML (update, delete and insert) sentences
            int nrows = stmt.executeUpdate();
            // it is important to commit changes
            conn.commit();
            return nrows;
        } catch (SQLException e) {
            // when there are problems updating returns -1
            return -1;
        }
    }

    /**
     * list contacts that contains text in name or telephone
     *
     * @param text searching text
     * @return list of contacts containing text in name or telephone
     */
    public ArrayList<Contact> searchContacts(String text) {
        ArrayList<Contact> result = new ArrayList<Contact>();
        PreparedStatement stmt;
        try {
            stmt = this.conn.prepareStatement("Select * From contactos Where nombre like ? Or telefono like ?");
            // adding wildcard characters to text
            stmt.setString(1, "%" + text + "%");
            stmt.setString(2, "%" + text + "%");
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                result.add(new Contact(rs.getString("nombre"), rs.getString("telefono")));
            }
        } catch (SQLException e) {
            // TODO: error handling searching
            e.printStackTrace();
        }
        return result;
    }

    /**
     * delete contact in database
     *
     * @param name name of the contact to be deleted
     */
    public void delete(String name) {
        try {
            PreparedStatement stmt = this.conn.prepareStatement("Delete From contactos Where nombre = ?");
            stmt.setString(1, name);
            stmt.executeUpdate();
            this.conn.commit();
        } catch (SQLException e) {
            // TODO: error handling deleting
            e.printStackTrace();
        }
    }
}
