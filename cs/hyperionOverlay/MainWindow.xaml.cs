using System.Diagnostics;
using System.Windows;

namespace hyperionOverlay
{
    public partial class MainWindow : Window
    {
        private Process _targetProcess;

        // Updated constructor to accept the path
        public MainWindow(string targetPath)
        {
            InitializeComponent();

            this.WindowStyle = WindowStyle.None;
            this.WindowState = WindowState.Maximized;
            this.ResizeMode = ResizeMode.NoResize;

            // Start the process immediately if a path was provided
            if (!string.IsNullOrEmpty(targetPath))
            {
                try
                {
                    _targetProcess = Process.Start(targetPath);
                }
                catch (System.Exception ex)
                {
                    MessageBox.Show($"Failed to start process: {ex.Message}");
                }
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if (_targetProcess != null && !_targetProcess.HasExited)
            {
                // Graceful close (simulates clicking 'X')
                bool sent = _targetProcess.CloseMainWindow();

                // Fallback: If it doesn't close in 3 seconds, force it
                if (!sent || !_targetProcess.WaitForExit(3000))
                {
                    _targetProcess.Kill();
                }
            }

            // Finally, close the overlay itself
            Application.Current.Shutdown();
        }
    }
}
