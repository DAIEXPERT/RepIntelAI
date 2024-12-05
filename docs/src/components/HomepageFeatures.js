import React from 'react';
import clsx from 'clsx';
import { Link } from 'react-router-dom';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Repintel Platform',
    Svg: require('../../static/img/repintel-logo.png').default,
    docLink: './docs/repintel/getting-started/introduction',
    description: (
      <>
        Repintel is an open-source platform designed to conduct in-depth online research and intelligence on various tasks.
      </>
    ),
  },
  {
    title: 'Multi-Agent Assistant',
    Svg: require('../../static/img/multi-agent.png').default,
    docLink: './docs/repintel/multi_agents/overview',
    description: (
      <>
        Discover how Repintel's AI agents work collaboratively to gather insights and produce comprehensive intelligence reports.
      </>
    ),
  },
  {
    title: 'Examples and Demos',
    Svg: require('../../static/img/examples.png').default,
    docLink: './docs/repintel/examples/overview',
    description: (
      <>
          Explore Repintel in action across different scenarios, showcasing its research capabilities and analytical precision.
      </>
    ),
  },
];

function Feature({Svg, title, description, docLink}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <img src={Svg} alt={title} height="60"/>
      </div>
      <div className="text--center padding-horiz--md">
        <Link to={docLink}>
            <h3>{title}</h3>
        </Link>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container" style={{marginTop: 30}}>
        <div className="row" style={{justifyContent: 'center'}}>
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
