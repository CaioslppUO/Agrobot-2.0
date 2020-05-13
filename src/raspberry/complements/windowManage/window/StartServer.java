package window;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.SystemColor;
import javax.swing.JButton;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import javax.swing.JLabel;
import java.awt.Insets;
import java.awt.Component;
import javax.swing.Box;
import java.awt.Font;
import java.awt.Color;
import javax.swing.border.BevelBorder;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.JSpinner;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.awt.event.ActionEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class StartServer extends JFrame {

	public JPanel contentPane;
	public JTextField textFieldServerIp;
	public JPanel panelTop;
	public JButton buttonBack;
	public JRadioButton buttonEnableSensors;
	public JRadioButton buttonEnableUart;
	public JRadioButton buttonEnableRelays;
	public JSpinner spinnerQuantityOfBoards;
	public JButton buttonStartServer;

	public StartServer(JFrame mainWindow) {
		setTitle("Launcher Config");
		setBackground(SystemColor.desktop);
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, 664, 790);
		contentPane = new JPanel();
		contentPane.setBackground(SystemColor.desktop);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(new BorderLayout(0, 0));
		
		panelTop = new JPanel();
		panelTop.setBorder(new BevelBorder(BevelBorder.LOWERED, null, null, null, null));
		panelTop.setBackground(SystemColor.desktop);
		contentPane.add(panelTop, BorderLayout.NORTH);
		GridBagLayout gbl_panelTop = new GridBagLayout();
		gbl_panelTop.columnWidths = new int[]{117, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		gbl_panelTop.rowHeights = new int[]{25, 35, 0};
		gbl_panelTop.columnWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
		gbl_panelTop.rowWeights = new double[]{0.0, 0.0, Double.MIN_VALUE};
		panelTop.setLayout(gbl_panelTop);
		
		Component horizontalStrut = Box.createHorizontalStrut(100);
		GridBagConstraints gbc_horizontalStrut = new GridBagConstraints();
		gbc_horizontalStrut.insets = new Insets(0, 0, 0, 5);
		gbc_horizontalStrut.gridx = 1;
		gbc_horizontalStrut.gridy = 1;
		panelTop.add(horizontalStrut, gbc_horizontalStrut);
		
		JLabel labelConfigLauncher = new JLabel("Configurar Inicializador");
		labelConfigLauncher.setForeground(new Color(255, 255, 255));
		labelConfigLauncher.setFont(new Font("Gargi-1.2b", Font.BOLD, 20));
		GridBagConstraints gbc_labelConfigLauncher = new GridBagConstraints();
		gbc_labelConfigLauncher.insets = new Insets(0, 0, 0, 5);
		gbc_labelConfigLauncher.gridx = 4;
		gbc_labelConfigLauncher.gridy = 1;
		panelTop.add(labelConfigLauncher, gbc_labelConfigLauncher);
		
		JPanel panel = new JPanel();
		panel.setBackground(SystemColor.desktop);
		contentPane.add(panel, BorderLayout.CENTER);
		panel.setLayout(null);
		
		buttonEnableSensors = new JRadioButton("Habilitar Sensores");
		buttonEnableSensors.setBackground(new Color(152, 251, 152));
		buttonEnableSensors.setBounds(44, 62, 166, 23);
		panel.add(buttonEnableSensors);
		
		buttonEnableUart = new JRadioButton("Habilitar Uart");
		buttonEnableUart.setBackground(new Color(152, 251, 152));
		buttonEnableUart.setBounds(44, 118, 166, 23);
		panel.add(buttonEnableUart);
		
		buttonEnableRelays = new JRadioButton("Habilitar Relés");
		buttonEnableRelays.setBackground(new Color(152, 251, 152));
		buttonEnableRelays.setBounds(44, 184, 166, 23);
		panel.add(buttonEnableRelays);
		
		JLabel labelServerIp = new JLabel("Server IP");
		labelServerIp.setForeground(new Color(255, 255, 255));
		labelServerIp.setFont(new Font("Droid Sans", Font.BOLD, 15));
		labelServerIp.setBounds(406, 38, 70, 15);
		panel.add(labelServerIp);
		
		textFieldServerIp = new JTextField();
		textFieldServerIp.addKeyListener(new KeyAdapter() {
			@Override
			public void keyReleased(KeyEvent e) {
				if(e.getKeyCode() == 10) {
					showConfigWindow(mainWindow);
				}
			}
		});
		textFieldServerIp.setBounds(381, 64, 114, 19);
		panel.add(textFieldServerIp);
		textFieldServerIp.setColumns(10);
		
		JLabel labelQuantityOfBoards = new JLabel("Quantidade de placas");
		labelQuantityOfBoards.setForeground(new Color(255, 255, 255));
		labelQuantityOfBoards.setFont(new Font("Droid Sans", Font.BOLD, 15));
		labelQuantityOfBoards.setBounds(348, 122, 172, 15);
		panel.add(labelQuantityOfBoards);
		
		spinnerQuantityOfBoards = new JSpinner();
		spinnerQuantityOfBoards.setBounds(522, 118, 39, 23);
		panel.add(spinnerQuantityOfBoards);
		
		buttonStartServer = new JButton("Iniciar Servidor");
		
		buttonStartServer.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				showConfigWindow(mainWindow);
			}
		});
		
		buttonStartServer.setBounds(236, 263, 140, 61);
		panel.add(buttonStartServer);
		
		buttonBack = new JButton("<- Voltar");
		buttonBack.setBounds(12, 392, 120, 25);
		panel.add(buttonBack);
		buttonBack.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				dispose();
				mainWindow.setVisible(true);
			}
		});
	}
	
	void showConfigWindow(JFrame mainWindow) {
		int uartNumber;
		String ip;
		boolean enableUart,enableSensors,enableRelays;
		
		uartNumber = Integer.parseInt(spinnerQuantityOfBoards.getValue().toString());
		if(uartNumber < 0) {
			uartNumber = 0;
		}else if(uartNumber > 2) {
			uartNumber = 2;
		}
		ip = textFieldServerIp.getText();
		if(ip.isEmpty()) {
			ip = "192.168.1.2";
		}
		enableUart = buttonEnableUart.isSelected();
		enableSensors = buttonEnableSensors.isSelected();
		enableRelays = buttonEnableRelays.isSelected();
		
		String command;
		
		command = "xfce4-terminal -e '/bin/sh -c \"sudo python3 ../Controller.py " + "enableSensors:" + enableSensors + " enableUart:" + enableUart + " serverIp:" + ip + " enableRelays:" + enableRelays + " uartAmount:" + uartNumber + ";read\"'";
		
		ProcessBuilder processBuilder = new ProcessBuilder();

		processBuilder.command("bash", "-c", command);

		try {

			Process process = processBuilder.start();

			StringBuilder output = new StringBuilder();

			BufferedReader reader = new BufferedReader(
					new InputStreamReader(process.getInputStream()));

			String line;
			while ((line = reader.readLine()) != null) {
				output.append(line + "\n");
			}
			int exitVal = process.waitFor();
			if (exitVal == 0) {
				System.out.println(output);
			} else {}
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		dispose();
		mainWindow.setVisible(true);
	}
}
