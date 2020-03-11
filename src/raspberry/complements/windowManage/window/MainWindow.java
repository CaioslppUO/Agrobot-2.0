package window;

import java.awt.EventQueue;

import javax.swing.JFrame;
import java.awt.SystemColor;
import java.awt.Toolkit;
import java.awt.BorderLayout;
import javax.swing.JLabel;
import java.awt.Color;
import java.awt.Font;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.border.SoftBevelBorder;
import javax.swing.border.BevelBorder;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MainWindow {

	public JFrame mainFrame;

	public MainWindow() {
		initialize();
	}

	private void initialize() {
		mainFrame = new JFrame();
		mainFrame.setIconImage(Toolkit.getDefaultToolkit().getImage(MainWindow.class.getResource("/resources/icon.png")));
		mainFrame.setTitle("Agrobot");
		mainFrame.getContentPane().setBackground(SystemColor.desktop);
		mainFrame.getContentPane().setLayout(new BorderLayout(0, 0));
		
		JPanel panelTop = new JPanel();
		panelTop.setBorder(new BevelBorder(BevelBorder.LOWERED, null, null, null, null));
		panelTop.setBackground(SystemColor.desktop);
		mainFrame.getContentPane().add(panelTop, BorderLayout.NORTH);
		
		JLabel labelMainMenu = new JLabel("Main Menu");
		panelTop.add(labelMainMenu);
		labelMainMenu.setFont(new Font("Gargi-1.2b", Font.BOLD, 30));
		labelMainMenu.setForeground(new Color(192, 192, 192));
		
		JPanel panelMiddle = new JPanel();
		panelMiddle.setBorder(new SoftBevelBorder(BevelBorder.LOWERED, null, null, null, null));
		panelMiddle.setBackground(SystemColor.desktop);
		mainFrame.getContentPane().add(panelMiddle, BorderLayout.CENTER);
		panelMiddle.setLayout(null);
		
		JLabel labelArrow1 = new JLabel("->");
		labelArrow1.setFont(new Font("Dialog", Font.BOLD, 22));
		labelArrow1.setBounds(87, 28, 70, 15);
		panelMiddle.add(labelArrow1);
		
		JButton buttonControl = new JButton("Controlar");
		buttonControl.setBounds(131, 26, 360, 25);
		panelMiddle.add(buttonControl);
		
		JButton buttonMission = new JButton("Missão");
		buttonMission.setBounds(131, 76, 360, 25);
		panelMiddle.add(buttonMission);
		
		JLabel labelArrow2 = new JLabel("->");
		labelArrow2.setFont(new Font("Dialog", Font.BOLD, 22));
		labelArrow2.setBounds(87, 78, 70, 15);
		panelMiddle.add(labelArrow2);
		
		JButton buttonConfig = new JButton("Configuração");
		buttonConfig.setBounds(131, 130, 360, 25);
		panelMiddle.add(buttonConfig);
		
		JLabel labelArrow3 = new JLabel("->");
		labelArrow3.setFont(new Font("Dialog", Font.BOLD, 22));
		labelArrow3.setBounds(87, 132, 70, 15);
		panelMiddle.add(labelArrow3);
		
		JButton buttonDebug = new JButton("Debug");
		buttonDebug.setBounds(131, 175, 360, 25);
		panelMiddle.add(buttonDebug);
		
		JLabel labelArrow4 = new JLabel("->");
		labelArrow4.setFont(new Font("Dialog", Font.BOLD, 22));
		labelArrow4.setBounds(87, 177, 70, 15);
		panelMiddle.add(labelArrow4);
		
		JButton buttonStartSever = new JButton("Inicializar Servidor");
		
		buttonStartSever.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				mainFrame.setVisible(false);
				EventQueue.invokeLater(new Runnable() {
					public void run() {
						try {
							StartServer frame = new StartServer(mainFrame);
							frame.setVisible(true);
						} catch (Exception e) {
							e.printStackTrace();
						}
					}
				});
			}
		});
		
		buttonStartSever.setBounds(131, 222, 360, 25);
		panelMiddle.add(buttonStartSever);
		
		JLabel labelArrow5 = new JLabel("->");
		labelArrow5.setFont(new Font("Dialog", Font.BOLD, 22));
		labelArrow5.setBounds(87, 224, 70, 15);
		panelMiddle.add(labelArrow5);
		
		JButton buttonExit = new JButton("Sair");
		buttonExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		buttonExit.setBounds(131, 340, 360, 25);
		panelMiddle.add(buttonExit);
		
		JLabel labelArrow6 = new JLabel("->");
		labelArrow6.setFont(new Font("Dialog", Font.BOLD, 22));
		labelArrow6.setBounds(87, 342, 70, 15);
		panelMiddle.add(labelArrow6);
		mainFrame.setBackground(SystemColor.desktop);
		mainFrame.setBounds(100, 100, 664, 792);
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
