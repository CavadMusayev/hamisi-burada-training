using System;
using System.Diagnostics;
using System.IO;
using netcore.template;

namespace Recorder_Module
{
    public class OBS_Application
    {
        public static void LaunchOBS()
        {
            string obsExecutable = CONSTANTlar.OBS_EXECUTABLE_LOCATION;
            string obsDirectory = Path.GetDirectoryName(obsExecutable);

            // Setup ProcessStartInfo with the correct working directory
            var startInfo = new ProcessStartInfo
            {
                FileName = obsExecutable,
                WorkingDirectory = obsDirectory,  // Set the working directory
                UseShellExecute = true, // Use ShellExecute when launching external applications
                WindowStyle = ProcessWindowStyle.Minimized,
                Arguments = "--disable-shutdown-check"
            };

            // Launch OBS
            try
            {
                // Check if any instance of OBS is running
                var obsProcesses = Process.GetProcessesByName("obs64");
                if (obsProcesses.Length > 0)
                {
                    Console.WriteLine("OBS is already running.");
                }
                else
                {
                    Console.WriteLine("OBS is not running. Launching OBS...");
                    Process.Start(startInfo);
                    Console.WriteLine("OBS launched successfully.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Failed to check or launch OBS: {ex.Message}");
            }
        }
    }
}