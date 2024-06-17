## 下载

mac 地址 https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-473.0.0-darwin-x86_64.tar.gz?hl=zh-cn

解压

```
➜  google-cloud-sdk ls
LICENSE             RELEASE_NOTES       bin                 completion.zsh.inc  deb                 install.sh          path.bash.inc       path.zsh.inc        proper
```

安装
```
./install.sh
```

安装过程

```
To help improve the quality of this product, we collect anonymized usage data and anonymized stacktraces when crashes are encountered; additional information is available at
<https://cloud.google.com/sdk/usage-statistics>. This data is handled in accordance with our privacy policy <https://cloud.google.com/terms/cloud-privacy-notice>. You may choose to opt in this collection now (by
choosing 'Y' at the below prompt), or at any time in the future by running the following command:

    gcloud config set disable_usage_reporting false

Do you want to opt-in (y/N)?  y

Beginning update. This process may take several minutes.


Your current Google Cloud CLI version is: 473.0.0
You will be upgraded to version: 475.0.0

┌─────────────────────────────────────────────────────────┐
│            These components will be updated.            │
├─────────────────────────────────┬────────────┬──────────┤
│               Name              │  Version   │   Size   │
├─────────────────────────────────┼────────────┼──────────┤
│ Google Cloud CLI Core Libraries │ 2024.05.03 │ 18.5 MiB │
│ gcloud cli dependencies         │ 2024.05.03 │ 16.6 MiB │
└─────────────────────────────────┴────────────┴──────────┘

The following release notes are new in this upgrade.
Please read carefully for information about new features, breaking changes,
and bugs fixed.  The latest full release notes can be viewed at:
  https://cloud.google.com/sdk/release_notes

475.0.0 (2024-05-07)
  Google Cloud CLI
      ▪ Enabled faster component update mode by default on macOS. This avoids
        making a backup copy of the installation directory when running certain
        gcloud components commands, which should significantly improve the time
        taken by these operations (including installation and updates).
        ◆ If for some reason this change causes problems, please file a bug
          report. One can temporarily revert to the legacy update mode via
          gcloud config set experimental/fast_component_update False or by
          setting the environment variable
          CLOUDSDK_EXPERIMENTAL_FAST_COMPONENT_UPDATE=False (it may be
          necessary to first reinstall the gcloud CLI either from scratch or by
          running gcloud components reinstall). Note that the faster update
          mode will eventually become the default on all platforms at which
          point the fast_component_update mode property will be removed.
        ◆ Since the gcloud CLI no longer makes a full copy of the
          installation directory to allow for this performance improvement,
          gcloud components restore has been deprecated. However, equivalent
          functionality can be achieved via gcloud components update
          --version=<previous version> or gcloud components reinstall,
          depending on whether one needs to restore an earlier version or
          reinstall the current version, respectively.

  Anthos Multi-Cloud
      ▪ Updated gcloud container attached clusters register to fail when
        using --has-private-issuer with --distribution=eks.

  Artifact Registry
      ▪ Fixed bug where gcloud artifacts docker upgrade migrate sometimes
        excluded bucket auth from generated IAM policies.

  Cloud Build
      ▪ Modified gcloud builds submit to support submitting a build with a
        Developer Connect GitRepositoryLink resource.

  Cloud Dataflow
      ▪ Promoted gcloud dataflow yaml run to GA.

  Cloud Datastream
      ▪ Fix bug where append only flag not recognized in
        BiQueryDestinationConfig.

  Cloud Firestore Emulator
      ▪ Release Cloud Firestore emulator v1.19.6
        ◆ Added --import-data and --export-on-exit flags.
        ◆ Fixed few bugs regarding transactions, including: read only
          commits, retriable transactions and contention errors on commits.

  Cloud NetApp
      ▪ Added flex as a --service-level option during gcloud netapp
        storage-pools create.

  Compute Engine
      ▪ Promoted dual stack IPv6 support for gcloud compute instances
        create-with-container and gcloud compute instance-templates
        create-with-container to GA.

  Network Connectivity
      ▪ Promote Regional API Endpoints to GA.
      ▪ Added --export-psc and --no-export-psc flags to gcloud
        network-connectivity hubs create and gcloud network-connectivity hubs
        update.

  Network Security
      ▪ Fixed gcloud network-security tls-inspection-policies import not
        recognizing minTlsVersion and tlsFeatureProfile.
      ▪ Fixed gcloud network-security tls-inspection-policies export not
        recognizing minTlsVersion and tlsFeatureProfile.

  Security Command Center
      ▪ Removed misleading documentation in gcloud scc findings create
        command that imply findings can be created at folder and project level.
        This command only allows findings to be created under an organization.

    Subscribe to these release notes at
    https://groups.google.com/forum/#!forum/google-cloud-sdk-announce
    (https://groups.google.com/forum/#!forum/google-cloud-sdk-announce).

474.0.0 (2024-04-30)
  Breaking Changes
      ▪ **(Cloud Run)** gcloud run jobs deploy is not working with source
        builds in this release. Run gcloud builds submit and then gcloud run
        jobs deploy with the generated image, or use Google Cloud CLI version
        472 or earlier.

  AI
      ▪ Added more choice options to --region flag of gcloud ai custom-jobs
        and gcloud ai hp-tunining-jobs, including: africa-south1,
        europe-west12, me-central1, me-central2 and us-east5.

  AlloyDB
      ▪ Updated gcloud beta alloydb clusters create-secondary to support
        automated backup policy.
      ▪ Added flags --maintenance-window-day and --maintenance-window-hour to
        configure preferred maintenance window for a cluster to commands gcloud
        alloydb clusters create and gcloud alloydb clusters update.
      ▪ Added flag --maintenance-window-any to remove preferred maintenance
        window for a cluster to gcloud alloydb clusters update.

  Artifact Registry
      ▪ Added gcloud artifacts generic upload to support uploading to a
        Generic Repository.
      ▪ Added gcloud artifacts generic download to support downloading to a
        Generic Repository.

  Cloud DNS
      ▪ Modified --description flag of gcloud dns managed-zones create to be
        optional instead of required. If not set, the managed zone's
        description will be empty.

  Cloud Monitoring
      ▪ Added --service-agent-auth flag to gcloud monitoring uptime commands.

  Compute Engine
      ▪ Added --tls-early-data flag to gcloud compute alpha/beta
        target-https-proxies create/update to Tls Early Data field in Target
        Https Proxy.
      ▪ Added gcloud compute project-zonal-metadata for managing project
        zonal metadata. Documentation of this feature is available at
        <https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-zonal-metadata>.
      ▪ Promoted --stack-type flag of gcloud compute interconnects
        attachments partner create to GA. Flag defines the stack type of
        partner interconnect attachment.
      ▪ Promoted --stack-type flag of gcloud compute interconnects
        attachments partner update to GA. Flag defines the stack type of
        interconnect attachment.
      ▪ Added producer-port argument when creating PSC NEGs. This is an
        optional field, and used to specify the port the PSC NEG will consume
        traffic from the PSC Producer.
      ▪ Promoted the flag of --partner-metadata and
        --partner-metadata-from-file to beta in:
        ◆ gcloud compute instance-templates create.
        ◆ gcloud compute instances create.
        ◆ gcloud compute instances update.
      ▪ Promoted gcloud compute instances add-partner-metadata command to
        beta.
      ▪ Promoted gcloud compute instances patch-partner-metadata command to
        beta.
      ▪ Promoted gcloud compute instances remove-partner-metadata command to
        beta.
      ▪ Promoted the flag of --view to beta in:
        ◆ gcloud compute instance-templates list
        ◆ gcloud compute instance-templates describe.
        ◆ gcloud compute instances list
        ◆ gcloud compute instances describe.

  Firebase Test Lab
      ▪ Promoted --resign flag of gcloud firebase test android run to GA.
        This flag allows clients to specify if Robo should re-sign the
        app-under-test APK.

  Kubernetes Engine
      ▪ Updated kubectl versions:
        ◆ kubectl.1.26 (1.26.15)
        ◆ kubectl.1.27 (1.27.13)
        ◆ kubectl.1.28 (1.28.9)
        ◆ kubectl.1.29 (1.29.4)
        ◆ kubectl.1.30 (1.30.0)
      ▪ Updated help text for --cluster-ipv4-cidr to clarify that this flag
        is not applicable in a Shared VPC setup.

  Network Services
      ▪ Promoted gcloud network-services service-lb-policies to GA.

    Subscribe to these release notes at
    https://groups.google.com/forum/#!forum/google-cloud-sdk-announce
    (https://groups.google.com/forum/#!forum/google-cloud-sdk-announce).

Do you want to continue (Y/n)?  y

╔════════════════════════════════════════════════════════════╗
╠═ Creating update staging area                             ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Uninstalling: Google Cloud CLI Core Libraries            ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Uninstalling: gcloud cli dependencies                    ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installing: Google Cloud CLI Core Libraries              ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Installing: gcloud cli dependencies                      ═╣
╠════════════════════════════════════════════════════════════╣
╠═ Creating backup and activating new installation          ═╣
╚════════════════════════════════════════════════════════════╝

Performing post processing steps...done.

Update done!

To revert your CLI to the previously installed version, you may run:
  $ gcloud components update --version 473.0.0

➜  ~ gcloud init
Welcome! This command will take you through the configuration of gcloud.

Settings from your current configuration [default] are:
core:
  disable_usage_reporting: 'False'

Pick configuration to use:
 [1] Re-initialize this configuration [default] with new settings
 [2] Create a new configuration
Please enter your numeric choice:
Please enter a value between 1 and 2:  1

Your current configuration has been set to: [default]

You can skip diagnostics next time by using the following flag:
  gcloud init --skip-diagnostics

Network diagnostic detects and fixes local network connection issues.
Checking network connection...done.
Reachability Check passed.
Network diagnostic passed (1/1 checks passed).

You must log in to continue. Would you like to log in (Y/n)?  y

Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=32555940559.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8085%2F&scope=openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-platform+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fappengine.admin+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fsqlservice.login+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcompute+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Faccounts.reauth&state=FRdH7J3W9bIHh6LPDLKP9ECEiIoZpG&access_type=offline&code_challenge=vybwa_2nXd4rzoDkamb9bpCrV5ZrqAih3Df3RZnB5_c&code_challenge_method=S256

You are logged in as: [yishenggudou@gmail.com].

Pick cloud project to use:
 [1] dafengstudio
 [2] dourawards
 [3] flexiwrapstore
 [4] gcp-haibo-test
 [5] longgangqu
 [6] newbeelabbroadcast
 [7] partridge-282911
 [8] timger-188109
 [9] youtube-upload-timger
 [10] Enter a project ID
 [11] Create a new project
Please enter numeric choice or text value (must exactly match list item):  2

Your current project has been set to: [dourawards].

Do you want to configure a default Compute Region and Zone? (Y/n)?  y

Which Google Compute Engine zone would you like to use as project default?
If you do not specify a zone via a command line flag while working with Compute Engine resources, the default is assumed.
 [1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b
 [11] us-west1-b
 [12] us-west1-c
 [13] us-west1-a
 [14] europe-west4-a
 [15] europe-west4-b
 [16] europe-west4-c
 [17] europe-west1-b
 [18] europe-west1-d
 [19] europe-west1-c
 [20] europe-west3-c
 [21] europe-west3-a
 [22] europe-west3-b
 [23] europe-west2-c
 [24] europe-west2-b
 [25] europe-west2-a
 [26] asia-east1-b
 [27] asia-east1-a
 [28] asia-east1-c
 [29] asia-southeast1-b
 [30] asia-southeast1-a
 [31] asia-southeast1-c
 [32] asia-northeast1-b
 [33] asia-northeast1-c
 [34] asia-northeast1-a
 [35] asia-south1-c
 [36] asia-south1-b
 [37] asia-south1-a
 [38] australia-southeast1-b
 [39] australia-southeast1-c
 [40] australia-southeast1-a
 [41] southamerica-east1-b
 [42] southamerica-east1-c
 [43] southamerica-east1-a
 [44] africa-south1-a
 [45] africa-south1-b
 [46] africa-south1-c
 [47] asia-east2-a
 [48] asia-east2-b
 [49] asia-east2-c
 [50] asia-northeast2-a
Did not print [72] options.
Too many options [122]. Enter "list" at prompt to print choices fully.
Please enter numeric choice or text value (must exactly match list item):  47

Your project default Compute Engine zone has been set to [asia-east2-a].
You can change it by running [gcloud config set compute/zone NAME].

Your project default Compute Engine region has been set to [asia-east2].
You can change it by running [gcloud config set compute/region NAME].

Created a default .boto configuration file at [/Users/timger/.boto]. See this file and
[https://cloud.google.com/storage/docs/gsutil/commands/config] for more
information about configuring Google Cloud Storage.
Your Google Cloud SDK is configured and ready to use!

* Commands that require authentication will use yishenggudou@gmail.com by default
* Commands will reference project `dourawards` by default
* Compute Engine commands will use region `asia-east2` by default
* Compute Engine commands will use zone `asia-east2-a` by default

Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [default]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the SDK like arg files and output formatting
* Run `gcloud cheat-sheet` to see a roster of go-to `gcloud` commands.
```


## 用法

```
Available command groups for gcloud:

  AI and Machine Learning
      ai                      Manage entities in Vertex AI.
      ai-platform             Manage AI Platform jobs and models.
      ml                      Use Google Cloud machine learning capabilities.
      ml-engine               Manage AI Platform jobs and models.
      notebooks               Notebooks Command Group.
      workbench               Workbench Command Group.

  API Platform and Ecosystems
      api-gateway             Manage Cloud API Gateway resources.
      apigee                  Manage Apigee resources.
      endpoints               Create, enable and manage API services.
      recommender             Manage Cloud recommendations and recommendation
                              rules.
      services                List, enable and disable APIs and services.

  Anthos CLI
      anthos                  Anthos command Group.

  Batch
      batch                   Manage Batch resources.

  Billing
      billing                 Manage billing accounts and associate them with
                              projects.

  CI/CD
      artifacts               Manage Artifact Registry resources.
      builds                  Create and manage builds for Google Cloud Build.
      deploy                  Create and manage Cloud Deploy resources.
      scheduler               Manage Cloud Scheduler jobs and schedules.
      tasks                   Manage Cloud Tasks queues and tasks.

  Compute
      app                     Manage your App Engine deployments.
      bms                     Manage Bare Metal Solution resources.
      compute                 Create and manipulate Compute Engine resources.
      container               Deploy and manage clusters of machines for running
                              containers.
      edge-cloud              Manage edge-cloud resources.
      functions               Manage Google Cloud Functions.
      run                     Manage your Cloud Run applications.
      vmware                  Manage Google Cloud VMware Engine resources.

  Data Analytics
      composer                Create and manage Cloud Composer Environments.
      data-catalog            Manage Data Catalog resources.
      dataflow                Manage Google Cloud Dataflow resources.
      dataplex                Manage Dataplex resources.
      dataproc                Create and manage Google Cloud Dataproc clusters
                              and jobs.
      looker                  Manage Looker resources.
      metastore               Manage Dataproc Metastore resources.
      pubsub                  Manage Cloud Pub/Sub topics, subscriptions, and
                              snapshots.

  Databases
      alloydb                 Create and manage AlloyDB databases.
      bigtable                Manage your Cloud Bigtable storage.
      database-migration      Manage Database Migration Service resources.
      datastore               Manage your Cloud Datastore resources.
      datastream              Manage Cloud Datastream resources.
      firestore               Manage your Cloud Firestore resources.
      memcache                Manage Cloud Memorystore Memcached resources.
      redis                   Manage Cloud Memorystore Redis resources.
      spanner                 Command groups for Cloud Spanner.
      sql                     Create and manage Google Cloud SQL databases.

  Identity
      active-directory        Manage Managed Microsoft AD resources.
      identity                Manage Cloud Identity Groups and Memberships
                              resources.

  Identity and Security
      access-approval         Manage Access Approval requests and settings.
      access-context-manager  Manage Access Context Manager resources.
      auth                    Manage oauth2 credentials for the Google Cloud
                              CLI.
      iam                     Manage IAM service accounts and keys.
      iap                     Manage IAP policies.
      kms                     Manage cryptographic keys in the cloud.
      org-policies            Create and manage Organization Policies.
      policy-intelligence     A platform to help better understand, use and
                              manage policies at scale.
      policy-troubleshoot     Troubleshoot Google Cloud Platform policies.
      privateca               Manage private Certificate Authorities on Google
                              Cloud.
      publicca                Manage accounts for Google Trust Services'
                              Certificate Authority.
      recaptcha               Manage reCAPTCHA Enterprise Keys.
      resource-manager        Manage Cloud Resources.
      resource-settings       Create and manage Resource Settings.
      secrets                 Manage secrets on Google Cloud.

  Management Tools
      apphub                  Manage App Hub resources.
      cloud-shell             Manage Google Cloud Shell.
      deployment-manager      Manage deployments of cloud resources.
      essential-contacts      Manage Essential Contacts.
      infra-manager           Manage Infra Manager resources.
      logging                 Manage Cloud Logging.
      organizations           Create and manage Google Cloud Platform
                              Organizations.
      projects                Create and manage project access policies.

  Mobile
      firebase                Work with Google Firebase.

  Monitoring
      monitoring              Manage Cloud Monitoring dashboards.

  Network Security
      network-security        Manage Network Security resources.

  Networking
      certificate-manager     Manage SSL certificates for your Google Cloud
                              projects.
      dns                     Manage your Cloud DNS managed-zones and
                              record-sets.
      domains                 Manage domains for your Google Cloud projects.
      edge-cache              Manage Media CDN resources.
      ids                     Manage Cloud IDS.
      network-connectivity    Manage Network Connectivity Center resources.
      network-management      Manage Network Management resources.
      network-services        Manage Network Services resources.
      service-directory       Command groups for Service Directory.
      service-extensions      Manage Service Extensions resources.
      telco-automation        Manage Telco Automation resources.

  Other
      immersive-stream        Manage Immersive Stream resources.
      workspace-add-ons       Manage Google Workspace Add-ons resources.

  SDK Tools
      components              List, install, update, or remove Google Cloud CLI
                              components.
      config                  View and edit Google Cloud CLI properties.
      emulators               Set up your local development environment using
                              emulators.
      source                  Cloud git repository commands.
      topic                   gcloud supplementary help.

  Security
      asset                   Manage the Cloud Asset Inventory.
      assured                 Read and manipulate Assured Workloads data
                              controls.
      scc                     Manage Cloud SCC resources.

  Serverless
      eventarc                Manage Eventarc resources.

  Solutions
      healthcare              Manage Cloud Healthcare resources.
      transcoder              Manage Transcoder jobs and job templates.

  Storage
      backup-dr               Manage Backup and DR resources.
      filestore               Create and manipulate Filestore resources.
      netapp                  Create and manipulate Cloud NetApp Files
                              resources.
      storage                 Create and manage Cloud Storage buckets and
                              objects.

  Tools
      workflows               Manage your Cloud Workflows resources.
      workstations            Manage Cloud Workstations resources.

  Transfer
      transfer                Manage Transfer Service jobs, operations, and
                              agents.

Available commands for gcloud:

  Other
      cheat-sheet             Display gcloud cheat sheet.
      docker                  *(DEPRECATED)*  Enable Docker CLI access to Google
                              Container Registry.
      survey                  Invoke a customer satisfaction survey for Google
                              Cloud CLI.

  SDK Tools
      feedback                Provide feedback to the Google Cloud CLI team.
      help                    Search gcloud help text.
      info                    Display information about the current gcloud
                              environment.
      init                    Initialize or reinitialize gcloud.
      version                 Print version information for Google Cloud CLI
                              components.
```