using System.Windows;

namespace hyperionOverlay
{
    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
        {
            string targetPath = e.Args.Length > 0 ? e.Args[0] : null;

            // Manually show the window and pass the path
            MainWindow mainWindow = new MainWindow(targetPath);
            mainWindow.Show();
        }
    }
}
