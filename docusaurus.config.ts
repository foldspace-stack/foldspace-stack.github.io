import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "Foldspace-Stack",
  tagline: "easy stack for small business",
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: "http://docs.foldspace.cn",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "foldspace-stack", // Usually your GitHub org/user name.
  projectName: "foldspace-stack.github.io", // Usually your repo name.

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            "https://github.com/foldspace-stack/foldspace-stack.github.io/tree/main/",
        },
        googleAnalytics: {
          trackingID: 'G-DMW09C95L0',
          anonymizeIP: true,
        },
        sitemap: {
          lastmod: "date",
          changefreq: "weekly",
          priority: 0.5,
          ignorePatterns: ["/tags/**"],
          filename: "sitemap.xml",
        },
        gtag: {
          trackingID: "G-999X9XX9XX",
          anonymizeIP: true,
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            "https://github.com/foldspace-stack/foldspace-stack.github.io/tree/main/",
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],
  headTags: [],
  themeConfig: {
    // Replace with your project's social card
    giscus: {
      repo: "foldspace-stack/foldspace-stack.github.io", // edit this
      repoId: "R_kgDOLplJxw", // edit this
      category: "General",
      categoryId: "DIC_kwDOLplJx84CezQ_", //
      lang: "zh-CN",
      theme: "noborder_dark",
    },
    metadata: [
      // Declare a <link> preconnect tag
      {
        name: "google-site-verification",
        content: "9kZMOhGH7ZLZ7uSCGZSM7N_IXDlXNKRC-v_G8mbOuGs",
      },
    ],
    image: "img/docusaurus-social-card.jpg",
    navbar: {
      title: "FoldSpace-Stack",
      logo: {
        alt: "FoldSpace",
        src: "img/foldspace-icon.png",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "简介",
        },
        { to: "/docs/category/技术平台", label: "技术平台", position: "left" },
        {
          to: "/docs/category/通用能力",
          label: "通用能力",
          position: "left",
        },
        {
          to: "/docs/category/产品和服务",
          label: "产品和服务",
          position: "left",
        },
        {
          to: "/docs/category/技术知识",
          label: "技术文章",
          position: "left",
        },
        { to: "/blog", label: "博客", position: "left" },
        {
          href: "https://foldspace.cn/",
          label: "Foldspace",
          position: "right",
        },
        {
          href: "https://open-ipaas.github.io/",
          label: "OpenIpaas",
          position: "right",
        },
        {
          href: "https://little-ddd.github.io/",
          label: "Little-DDD",
          position: "right",
        },
        {
          href: "https://github.com/foldspace-stack",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "light",
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Tutorial",
              to: "/docs/intro",
            },
            {
              label: "foldspace",
              href: "http://docs.foldspace.cn",
            },
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "Stack Overflow",
              href: "https://stackoverflow.com/questions/tagged/docusaurus",
            },
            {
              label: "Discord",
              href: "https://discordapp.com/invite/docusaurus",
            },
            {
              label: "Twitter",
              href: "https://twitter.com/docusaurus",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "Blog",
              to: "/blog",
            },
            {
              label: "GitHub",
              href: "https://github.com/foldspace-stack/foldspace-stack.github.io",
            },
            {
              label: "Ci",
              href: "https://github.com/foldspace-stack/foldspace-stack.github.io/actions/workflows/static.yml",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Foldspace-Stack group, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
