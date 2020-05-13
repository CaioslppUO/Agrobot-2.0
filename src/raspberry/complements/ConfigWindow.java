package agrobotConfigWindow;

import java.awt.EventQueue;

import javax.swing.JFrame;
import java.awt.Color;
import java.awt.GridBagLayout;
import javax.swing.JButton;
import java.awt.GridBagConstraints;
import javax.swing.JPanel;
import java.awt.Insets;
import javax.swing.JRadioButton;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.Component;
import javax.swing.Box;
import javax.swing.JSpinner;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.awt.event.ActionEvent;

public class ConfigWindow {

	private JFrame frmAgrobotConfigLauncher;
	private JTextField textFielIP;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ConfigWindow window = new ConfigWindow();
					window.frmAgrobotConfigLauncher.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public ConfigWindow() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmAgrobotConfigLauncher = new JFrame();
		frmAgrobotConfigLauncher.getContentPane().setBackground(Color.LIGHT_GRAY);
		frmAgrobotConfigLauncher.getContentPane().setLayout(null);
		
		JButton buttonLaunch = new JButton("Launch");
		
		buttonLaunch.setBounds(163, 27, 132, 40);
		frmAgrobotConfigLauncher.getContentPane().add(buttonLaunch);
		
		JRadioButton buttonUart = new JRadioButton("Enable Uarts");
		buttonUart.setBackground(Color.LIGHT_GRAY);
		buttonUart.setBounds(18, 100, 149, 23);
		frmAgrobotConfigLauncher.getContentPane().add(buttonUart);
		
		JRadioButton buttonSensors = new JRadioButton("Enable Sensors");
		buttonSensors.setBackground(Color.LIGHT_GRAY);
		buttonSensors.setBounds(18, 138, 149, 23);
		frmAgrobotConfigLauncher.getContentPane().add(buttonSensors);
		
		JRadioButton buttonRelays = new JRadioButton("Enable Relays");
		buttonRelays.setBackground(Color.LIGHT_GRAY);
		buttonRelays.setBounds(18, 180, 149, 23);
		frmAgrobotConfigLauncher.getContentPane().add(buttonRelays);
		
		JLabel labelIP = new JLabel("IP");
		labelIP.setBounds(335, 100, 70, 15);
		frmAgrobotConfigLauncher.getContentPane().add(labelIP);
		
		textFielIP = new JTextField();
		textFielIP.setBounds(291, 127, 114, 19);
		frmAgrobotConfigLauncher.getContentPane().add(textFielIP);
		textFielIP.setColumns(10);
		
		JLabel labelUartN = new JLabel("Uart Nº");
		labelUartN.setBounds(314, 158, 70, 15);
		frmAgrobotConfigLauncher.getContentPane().add(labelUartN);
		
		JSpinner spinnerUartN = new JSpinner();
		spinnerUartN.setBounds(314, 182, 57, 31);
		frmAgrobotConfigLauncher.getContentPane().add(spinnerUartN);
		
		buttonLaunch.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				int uartNumber;
				String ip;
				boolean enableUart,enableSensors,enableRelays;
				
				uartNumber = Integer.parseInt(spinnerUartN.getValue().toString());
				if(uartNumber < 0) {
					uartNumber = 0;
				}else if(uartNumber > 2) {
					uartNumber = 2;
				}
				ip = textFielIP.getText();
				if(ip.isEmpty()) {
					ip = "192.168.1.2";
				}
				enableUart = buttonUart.isSelected();
				enableSensors = buttonSensors.isSelected();
				enableRelays = buttonRelays.isSelected();
				
				String command;
				
				command = "xfce4-terminal -e '/bin/sh -c \"sudo python3 ../Controller.py " + "enableSensors:" + enableSensors + " enableUart:" + enableUart + " serverIp:" + ip + " enableRelays:" + enableRelays + " uartAmount:" + uartNumber + " " + ";read\"'";

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
						System.exit(0);
					} else {}
				} catch (IOException e) {
					e.printStackTrace();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				
			}
		});
		
		frmAgrobotConfigLauncher.setBackground(Color.LIGHT_GRAY);
		frmAgrobotConfigLauncher.setTitle("AgroBot Config Launcher");
		frmAgrobotConfigLauncher.setBounds(100, 100, 450, 300);
		frmAgrobotConfigLauncher.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
