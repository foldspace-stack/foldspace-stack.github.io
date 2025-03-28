import clsx from "clsx";
import Heading from "@theme/Heading";
import styles from "./styles.module.css";

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<"svg">>;
  imgSrc?:string,
  videoSrc?:string,
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: "AI私有化部署解决方案",
    Svg: require("./svgs/item1.svg").default,
    imgSrc:require("./svgs/item1.webp").default,
    description: (
      <>
        <p>√ 自主可控的垂直领域大模型</p>
        <p>√ 企业级知识库智能重构</p>
        <p>√ 私有云+混合云双轨部署</p>
        <p>√ GDPR/等保三级合规架构</p>
        <p>"让每个企业拥有专属的AI智慧中枢"</p>
      </>
    ),
  },
  {
    title: "智能ERP&软件定制",
    Svg: require("./svgs/item2.svg").default,
    imgSrc:require("./svgs/item2.webp").default,

    description: (
      <>
        <p>√ 行业化深度定制（制造/零售/医疗专属方案）</p>
        <p>√ 业务流程数字孪生建模</p>
        <p>√ BI智能决策中台</p>
        <p>√ 供应链金融协同系统</p>
        <p>"深度定制贴身服务,成本优势"</p>
      </>
    ),
  },
  {
    title: "MCN全域IP孵化",
    Svg: require("./svgs/item3.svg").default,
    imgSrc:require("./svgs/item3.webp").default,
    description: (
      <>
        <p>√ 达人矩阵生态构建 </p>
        <p>√ 短视频工业化生产体系</p>
        <p>√ 品牌IP元宇宙升级</p>
        <p>√ 电商全链路变现设计</p>
        <p>"从流量到留量的内容商业新基建"</p>
      </>
    ),
  },
];

function Feature({ title, Svg, imgSrc,videoSrc,description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")} >
      <div className="text--center" style={{marginBottom:52}}>
        {imgSrc?<img className="feature-img" src={imgSrc}/>: <Svg className={styles.featureSvg} role="img" />}
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
