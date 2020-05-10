package com.company;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

/**
 * address book main window
 */
public class Principal extends JFrame {
    // data
    private AddressBook myAddressBook;
    // components
    private JButton btnExit;
    private JTextField txtSearch;
    private JTable tblResult;
    private JButton btnSearch;
    private JButton btnInsert;
    private JButton btnDelete;
    private JButton btnUpdate;
    private JButton btnList;

    /**
     * default constructor with window title
     *
     * @param title window title
     * @throws HeadlessException
     */
    public Principal(String title) throws HeadlessException {
        super(title);
        initData();
        initComponents();
    }

    /**
     * initialize address book data
     */
    private void initData() {
        this.myAddressBook = new AddressBook("agenda", "root", "root");
    }

    /**
     * initialize widgets
     */
    private void initComponents() {
        Container panel = this.getContentPane();

        // layout assignment
        panel.setLayout(new GridBagLayout());

        GridBagConstraints c = new GridBagConstraints();
        c.fill = GridBagConstraints.HORIZONTAL;
        // additional gap between cells
        c.insets = new Insets(2, 2, 2, 2);

        // button creation
        this.btnExit = new JButton();
        this.btnExit.setText("Exit");
        // position set
        c.gridx = 5;
        c.gridy = 3;
        // add button to the windows panel
        panel.add(btnExit, c);
        // action listener
        this.btnExit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });

        this.btnSearch = new JButton();
        this.btnSearch.setText("Search");
        c.gridx = 4;
        c.gridwidth = 2;
        c.gridy = 0;
        panel.add(this.btnSearch, c);
        this.btnSearch.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                searchContacts();
            }
        });

        this.btnInsert = new JButton();
        this.btnInsert.setText("Insert");
        c.gridx = 0;
        c.gridwidth = 1;
        c.gridy = 3;
        panel.add(this.btnInsert, c);
        this.btnInsert.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {

            }
        });


        this.btnDelete = new JButton();
        this.btnDelete.setText("Delete");
        c.gridx = 1;
        c.gridy = 3;
        panel.add(this.btnDelete, c);
        this.btnDelete.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                deleteContact();
            }
        });

        this.btnList = new JButton();
        this.btnList.setText("List");
        c.gridx = 3;
        c.gridy = 3;
        panel.add(this.btnList, c);
        this.btnList.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                listContacts();
            }
        });

        // using empty label to left blank spaces in grid
        JLabel emptyLabel = new JLabel("      ");
        c.gridx = 4;
        c.gridy = 3;
        panel.add(emptyLabel, c);

        this.txtSearch = new JTextField();
        this.txtSearch.setText("");
        c.gridx = 0;
        c.gridwidth = 4;
        c.gridy = 0;
        panel.add(this.txtSearch, c);

        this.tblResult = new JTable();
        c.gridx = 0;
        c.gridwidth = 6;
        c.gridy = 1;
        // needed to show the columns names
        panel.add(new JScrollPane(this.tblResult), c);
        // avoid multiple table row selection
        this.tblResult.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        // prepare table for address book data
        // empty data
        String[][] emptyData = new String[][]{};
        // column names
        String[] columnNames = new String[]{"Name", "Telephone"};
        // JTable stores values in model
        DefaultTableModel tableModel = new DefaultTableModel(emptyData, columnNames);
        this.tblResult.setModel(tableModel);
        // add data to table
        listContacts();

        // to get the old value when changing the table:
        // https://tips4java.wordpress.com/2009/06/07/table-cell-listener/
        Action action = new AbstractAction() {
            public void actionPerformed(ActionEvent e) {
                TableCellListener tcl = (TableCellListener) e.getSource();
                updateContact(tcl);
            }
        };
        TableCellListener tcl = new TableCellListener(this.tblResult, action);

        // adjust frame to components added
        this.pack();
    }

    /**
     * search contacts containing text placed in txtSearch widget
     */
    private void searchContacts() {
        ArrayList<Contact> contactList = this.myAddressBook.searchContacts(this.txtSearch.getText());
        fillTable(contactList);
    }

    /**
     * fills table with every contact in database
     */
    private void listContacts() {
        // clear search text
        this.txtSearch.setText("");
        ArrayList<Contact> contactList = this.myAddressBook.getContacts();
        fillTable(contactList);
    }

    /**
     * fills table with contact list
     *
     * @param contactList list of contacts to show
     */
    private void fillTable(ArrayList<Contact> contactList) {
        clearTable();
        // table stores data in model
        DefaultTableModel model = (DefaultTableModel) this.tblResult.getModel();
        for (Contact contact : contactList) {
            String[] newRow = new String[]{contact.getName(), contact.getTelephone()};
            model.addRow(newRow);
        }
    }

    // TODO: show modal dialog to get new contact information
    private void insertContact() {
    }

    /**
     * update contact information in database
     *
     * @param tcl listener containing old value after changing table cell
     * @return number of contacts affected, -1 if error updating
     */
    private int updateContact(TableCellListener tcl) {
        int row = tcl.getRow();
        int col = tcl.getColumn();
        String oldName = (String) this.tblResult.getModel().getValueAt(row, 0);
        String newName = (String) this.tblResult.getModel().getValueAt(row, 0);
        String newTelephone = (String) this.tblResult.getModel().getValueAt(row, 1);
        // oldValue only needed when updating name
        if (col == 0)
            oldName = (String) tcl.getOldValue();
        int result = this.myAddressBook.update(oldName, newName, newTelephone);
        // if there is any error updating database change is denied
        if (result <= 0) {
            DefaultTableModel model = (DefaultTableModel) this.tblResult.getModel();
            model.setValueAt(tcl.getOldValue(), row, col);
        }
        return result;
    }

    /**
     * delete contact in database
     */
    private void deleteContact() {
        String name = (String) this.tblResult.getModel().getValueAt(this.tblResult.getSelectedRow(), 0);
        myAddressBook.delete(name);
        // if there is text in txtSearch repeat search, if not list every contact
        if (txtSearch.equals(""))
            listContacts();
        else
            searchContacts();
    }

    /**
     * clear table
     */
    private void clearTable() {
        DefaultTableModel model = (DefaultTableModel) this.tblResult.getModel();
        int rows = model.getRowCount();
        // reverse iteration over the table contents for deleting
        for (int i = rows - 1; i >= 0; i--)
            model.removeRow(i);
    }

    /**
     * create and show main window
     *
     * @param args not using command line arguments
     */
    public static void main(String[] args) {
        JFrame window = new Principal("My Address Book");
        window.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        window.setVisible(true);
    }
}
